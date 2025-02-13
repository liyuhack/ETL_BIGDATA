from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, when, count, trim, lower, to_timestamp, isnan
from pyspark.sql.types import FloatType
from pyspark.sql.functions import date_format
import os

# Initialize Spark Session
spark = SparkSession.builder.appName("ElectronicsDataCleaning").getOrCreate()

# Load Dataset
df = spark.read.csv("./data/raw/kz.csv", header=True, inferSchema=True)

# Count rows before cleaning
total_rows_before = df.count()

# 1. Handle Missing Values
# Count the number of nulls or NaNs for each specified column
null_counts = {}
columns_to_check = ["event_time", "order_id", "product_id", "user_id"]

for col_name in columns_to_check:
    null_counts[col_name] = df.filter(col(col_name).isNull()).count()

df = df.dropna(subset=["event_time", "order_id", "product_id", "user_id"])
price_median = df.approxQuantile("price", [0.5], 0.05)[0]
df = df.fillna({"price": price_median})

# 2. Remove Duplicates
duplicate_count_before = df.count() - df.dropDuplicates(subset=["order_id", "product_id"]).count() # Count duplicates before cleaning
df = df = df.dropDuplicates(subset=["order_id", "product_id"])  # cleaning rows

# 3. Validate User IDs
df = df.filter(col("user_id").cast("int").isNotNull() & (col("user_id") > 0))

# # 3. Format Timestamps
# df = df.withColumn("event_time", to_timestamp("event_time"))

# 4. Add a new column for the day of the week
df = df.withColumn("day_of_week", date_format(col("event_time"), "E"))

# 5. Standardize Text Fields
df = df.withColumn("category_code", trim(lower(col("category_code"))))
df = df.withColumn("brand", trim(lower(col("brand"))))

# # 5. Handle Outliers in Prices
# Q1, Q3 = df.approxQuantile("price", [0.25, 0.75], 0.05)
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# noised_data_before = df.filter((col("price") < lower_bound) | (col("price") > upper_bound)).count()
# print(f"Noised Data Count Before Cleaning: {noised_data_before}")

# df = df.filter((col("price") >= lower_bound) & (col("price") <= upper_bound))
# noised_data_after = df.filter((col("price") < lower_bound) | (col("price") > upper_bound)).count()
# print(f"Noised Data Count After Cleaning: {noised_data_after}")

# 6. Encode Categories
df = df.withColumn(
    "category_encoded", 
    when(col("category_code").startswith("electronics"),"electronics")
    .when(col("category_code").startswith("furniture"), "furniture")
    .when(col("category_code").startswith("computers"), "computers")
    .when(col("category_code").startswith("kids"), "kids")
    .when(col("category_code").startswith("apparel"), "apparel")
    .when(col("category_code").startswith("stationery"), "stationery")
    .otherwise("others")  # Default value for non-matching categories
)

# Count rows after cleaning
total_rows_after = df.count() 
print(f"Total Rows Before Cleaning: {total_rows_before}")
for column, count in null_counts.items():
    print(f"Number of nulls before cleaning in {column}: {count}")
print(f"Duplicate Count Before Cleaning: {duplicate_count_before}")
print(f"Total Rows After cleaing: {total_rows_after}")

# Save Cleaned Dataset with Specific Filename
output_dir = "./data/cleaned/"
output_file = "cleaned_electronics_data.csv"

df.coalesce(1).write.csv(output_dir, header=True, mode="overwrite")

# Rename the single part file to the desired filename
output_path = os.path.join(output_dir, output_file)
part_file = [f for f in os.listdir(output_dir) if f.startswith("part-")][0]  # Find the part file
os.rename(os.path.join(output_dir, part_file), output_path)

print(f"Cleaned data saved as: {output_path}")
