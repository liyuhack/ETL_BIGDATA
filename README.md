Name: Biruk Damte ID: DBUR/0344/13

---

# E-commerce Data Pipeline Project 🚀  

This project demonstrates an end-to-end data pipeline for analyzing an elctornics purchase e-commerce dataset. The pipeline involves **data extraction**, **cleaning and transformation**, **storage in DuckDB**, and **visualization using Power BI**.  

---

## 🌟 Features  

- **Automated Dataset Extraction**: Downloads datasets directly from Kaggle using the `kagglehub` Python package.  
- **Data Transformation**: Cleans, validates, and prepares data using PySpark.  
- **Efficient Storage**: Utilizes DuckDB for fast querying and lightweight storage.  
- **Interactive Dashboards**: Visualizes key e-commerce metrics like sales trends and customer segmentation with Power BI.  

---

## 📂 Workflow Overview  

1. **Extract**: Download dataset from Kaggle.  
2. **Transform**:  
   - Handle missing values.  
   - Remove duplicates.  
   - Standardize and encode categories.  
   - Add derived fields (e.g., day of the week).  
3. **Load**: Save cleaned data into a DuckDB database.  
4. **Visualize**: Build interactive dashboards in Power BI by connecting directly to the DuckDB database.  

---

## 📋 Prerequisites  

### 1. Python Libraries  
- KaggleHub  
- PySpark  
- Pandas  
- DuckDB  

### 2. Hadoop Dependency (for PySpark)  
PySpark requires Hadoop dependencies to function properly. Follow the steps below to set it up:  

1. **Download `winutils.exe` for Hadoop**  
   Download from [this repository](https://github.com/cdarlint/winutils). Extract the folder `hadoop-3.2.2/bin` and place it in a directory, e.g., `C:\hadoop\bin\winutils.exe`.  

2. **Set Environment Variables**  
   - Add a new system variable:  
     - **Variable name**: `HADOOP_HOME`  
     - **Variable value**: `C:\hadoop` (or the path where you placed `winutils.exe`).  
   - Add `C:\hadoop\bin` to the **Path** system variable.  

3. **Verify Setup**  
   - Open Command Prompt and run:  
     ```  
     echo %HADOOP_HOME%  
     ```  
     You should see `C:\hadoop` (or your chosen path).  
   - Run:  
     ```  
     winutils.exe chmod 777 /tmp  
     ```  
     If no errors occur, the setup is complete.  

4. **Restart Your System**  

For detailed instructions, refer to [Hadoop Setup for PySpark](https://github.com/cdarlint/winutils).  

---

### 3. Power BI Integration with DuckDB  

Power BI supports DuckDB integration, allowing seamless data visualization. Follow this [guide](https://motherduck.com/docs/integrations/bi-tools/powerbi/) to set up Power BI with DuckDB.  

---

### 4. How to run and get the result  
Follow the steps below to download, clean, load, and visualize the data:  

1. **clone the repository**  
   - run this in your terminal 
   ```
   git clone https://github.com/liyuhack/ETL_BIGDATA.git
   ```
   - then change directory 
   ```
   cd ETL_BIGDATA
   ```
   - After that to open vscode editor 
   ```
   code .
   ```  

2. **Get all dependencies mentioned above and configure them**  
   - install python packages by running the following commands sequencially:  
     ```
     pip install duckdb
     ```  
     ```
     pip install kagglehub
     ``` 
     ```
     pip install pandas
     ```
     ```
     pip install pyspark
     ```

3. **Run the files**  
   - step 1: Run
     `step_1_download_data_from_kaggle.py` 
     This python code downloads and saves the data to `data/raw` directory
   - step 2: Run  
     `step_2_transform_data.py` 
     This python code clean and transforms the data and save the csv file to `data/cleaned` directory
   - step 3: Run 
     `step_3_load_to_duckdb.py` 
     This python code loads the cleaned data to duckdb database and saves the db file to `data/duckdb` directory

4. **Visualize**  
To visualize the cleaned and loaded data, install power BI from microsoft store. For details setup process,
refer to [guide](https://motherduck.com/docs/integrations/bi-tools/powerbi/) . 

---

## 📊 Insights & Dashboards  

Using Power BI, the following insights were visualized:  

- Sales trends over time.  
- Customer segmentation based on purchase history.  
- Popular product categories and brands.  
- Correlations between day of the week and sales activity.  

The dashboards provide actionable insights for e-commerce businesses.  

---

## 💡 Key Challenges  

1. **PySpark Setup**: Configuring Hadoop for PySpark compatibility was a hurdle. The detailed setup instructions (above) solved this issue.  
2. **Power BI and DuckDB Integration**: Initial challenges in connecting Power BI to DuckDB were resolved using [MotherDuck's documentation](https://motherduck.com/docs/integrations/bi-tools/powerbi/).  

---

## 🤝 Dependencies  

- [KaggleHub](https://pypi.org/project/kagglehub/)  
- [PySpark](https://spark.apache.org/docs/latest/api/python/)  
- [DuckDB](https://duckdb.org/)  
- [Pandas](https://pandas.pydata.org/)  

---

## 📁 Directory Structure  

```plaintext  
├── data/  
│   ├── raw/            # Raw dataset downloaded from Kaggle  
│   ├── cleaned/        # Cleaned dataset (CSV format)  
│   └── duckdb/         # DuckDB database  
├── ETL process documentation.pdf            # PROJECT DOCUMENTATION 
├── .gitignore                               # GIT FILE 
├── README.md                                # REPO README FILE  
├── step_1_download_data_from_kaggle.py      # DOWNLOADS DATA FROM KAGGLE  
├── step_2_transform_data.py                 # TRANSFORMS DATA  
├── step_3_load_to_duckdb.py                 # LOAD DATA TO DATABASE  
└── step_4_power_bi_analysis.pbix            # POWER BI FILE  
```  

---

## 📚 Resources  

- [Download Hadoop Winutils](https://github.com/cdarlint/winutils)  
- [Power BI + DuckDB Integration](https://motherduck.com/docs/integrations/bi-tools/powerbi/)  

---

## 🏆 Acknowledgments  

Special thanks to **PySpark** and **Power BI** communities for their helpful resources.  

---

Make your data work for you. 🚀