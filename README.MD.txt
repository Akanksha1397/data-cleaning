1. Take a Kaggle dataset of Sales Data
2. For missing value : used used isnull(). Then found out some of columns has missing value > 50% such as "ADDRESSLINE2","STATE","TERRITORY" and one column POSTAL CODE which has 2.6%.
3. Drop these columns ""ADDRESSLINE2","STATE","TERRITORY" using .drop()
4. For column POSTAL CODE: Filled using .fillna("Not Available")
5. For duplicates use .duplicated() as this data does not contain dupicates but for safer side i used Remove duplicates but keep the LAST occurrence using .drop_duplicates(keep='last')
6. For standardize some column are standardize in lower, upper, captialsize  and title str.lower() etc.. and for space .strip() has been used 
7. For date: Orderdate column has been formatted using pd.to_datetime for consistency.
8. Rename column in UPPERCASE 
9. Fix data type some column in string, some in category and some in numerical. 