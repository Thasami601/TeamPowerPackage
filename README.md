# TeamPowerPackage
This package will collate eskom data and give insight into the major issues affecting the power utility
This will be achieved through the collection of functions encoded in this package

# Eskom Insights
Building functions using python which will process both numeric and text data.

# Prerequisites
+ numpy and pandas library

# Installing
+ import numpy as np
+ import pandas as pd
##### Building package locally
+ `python setup.py sdist`
##### Installing package from Github
+ `pip install git+https://github.com/Thasami601/TeamPowerPackage`
##### Updating package from Github
+ `pip install --upgrade git+https://github.com/Thasami601/TeamPowerPackage`

# Details
- Function 1: returns metric summary statistics in a dictionary format.

_**Expected Output**_:

```python
dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'var': 108160153.17,
                                   'std': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}
 ```

- Function 2: returns five number summary statistics in a dictionary format.

_**Expected Output:**_

```python
five_num_summary(gauteng) == {
    'max': 39660.0,
    'median': 24403.5,
    'min': 8842.0,
    'q1': 18653.0,
    'q3': 36372.0
}

```

- Function 3: returns a list of strings of 'dates' in yyyy-mm-dd format.

_**Expected Output:**_

```python
date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']
```

- Function 4: returns a modified dataframe with municipality and hashtags columns corresponding to every tweet.

_**Expected Outputs:**_ 

```python

extract_municipality_hashtags(twitter_df.copy())

```
> <table class="dataframe" border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Tweets</th>
      <th>Date</th>
      <th>municipality</th>
      <th>hashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>@BongaDlulane Please send an email to mediades...</td>
      <td>2019-11-29 12:50:54</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>@saucy_mamiie Pls log a call on 0860037566</td>
      <td>2019-11-29 12:46:53</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>@BongaDlulane Query escalated to media desk.</td>
      <td>2019-11-29 12:46:10</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Before leaving the office this afternoon, head...</td>
      <td>2019-11-29 12:33:36</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...</td>
      <td>2019-11-29 12:17:43</td>
      <td>NaN</td>
      <td>[#eskomfreestate, #mediastatement]</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>195</th>
      <td>Eskom's Visitors Centresâ€™ facilities include i...</td>
      <td>2019-11-20 10:29:07</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>196</th>
      <td>#Eskom connected 400 houses and in the process...</td>
      <td>2019-11-20 10:25:20</td>
      <td>NaN</td>
      <td>[#eskom, #eskom, #poweringyourworld]</td>
    </tr>
    <tr>
      <th>197</th>
      <td>@ArthurGodbeer Is the power restored as yet?</td>
      <td>2019-11-20 10:07:59</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>198</th>
      <td>@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...</td>
      <td>2019-11-20 10:07:41</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>199</th>
      <td>RT @GP_DHS: The @GautengProvince made a commit...</td>
      <td>2019-11-20 10:00:09</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

- Function 5: returns a datframe with dates of tweets and corresponding number of tweets for a particular day.
- Function 6: returns a dataframe with 'Split Tweets' added column.
- Function 7: returns a modified dataframe with 'Without Stop Words' added column.

# Built With
- VS Code
- Python

# Data used to extract Eskom Insights
- See Data_Links_and_variables_info folder in TeamPowerPackage

# Authors
+ Mlangeni Simangaliso
+ Mogano Lebogang
+ Myeni Nkululeko
+ Soobyah Thasami
+ Tshabangu Cindy

# License
+ This project is licensed under the MIT License

# Acknowledgments
+ African Bank 
##### Thank you African Bank for giving us this opportunity.
+ Explore Data Science Academy
+ Joanne Moonsamy (Supervisor)
+ Ridha (Co- Supervisor)
##### Thank you for consistent guidance and support.
+ Jonathan G and Ridha (Setting up Github)
