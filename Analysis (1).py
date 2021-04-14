{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "cell_id": "00000-7b92686f-5567-4d2d-b6c9-cf7233b7c0a6",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 9,
    "execution_start": 1618346168405,
    "source_hash": "d99a5308",
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import sweetviz as sv\n",
    "from matplotlib import cm\n",
    "import seaborn as sns\n",
    "import scipy.stats as st\n",
    "import statsmodels as sm\n",
    "from scipy.stats import pearsonr\n",
    "%matplotlib widget\n",
    "#url, title, author, num_reviews, num_ratings, avg_rating, num_pages, original_publish_year, series, genres, awards, places"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00001-0c1ce99e-8094-4b61-b02c-3de96516f557",
    "deepnote_cell_type": "text-cell-h1",
    "tags": []
   },
   "source": [
    "# PREPROCESSING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "cell_id": "00001-11b176a9-7d43-4095-b161-27bec0d71e23",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 3,
    "execution_start": 1618325082432,
    "source_hash": "a26d370e",
    "tags": []
   },
   "outputs": [],
   "source": [
    "def preprocessing (df):\n",
    "\n",
    "    \n",
    "    print(df)\n",
    "    \n",
    "    #number of awards\n",
    "    awards_number = [len(awards.split(',')) for awards in df['Genre'] ]\n",
    "    df[\"award_number\"]= awards_number\n",
    "\n",
    "    #normalizations\n",
    "    maxr=df['avg_ratings'].max()\n",
    "    minr =df['avg_ratings'].min()\n",
    "    meanr= df['avg_ratings'].mean()\n",
    "    #mean_normalization\n",
    "    df['mean_norm_ratings'] = (df['avg_ratings']- meanr) / (maxr- minr)\n",
    "\n",
    "    #min-max normalization\n",
    "    df['min_max'] = 10 + ((df.avg_ratings-minr)/(maxr-minr))*90\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00003-e7d27fab-b288-4b55-a144-e318434e8b88",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "### Test Data 100 books\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "cell_id": "00003-1a9da32f-d37c-4bac-8a5e-0d18d16c2c4b",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 87,
    "execution_start": 1618314114980,
    "source_hash": "44b39a8b",
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/shared-libs/python3.7/py-core/lib/python3.7/site-packages/ipykernel_launcher.py:10: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  # Remove the CWD from sys.path while we load stuff.\n",
      "/shared-libs/python3.7/py-core/lib/python3.7/site-packages/ipykernel_launcher.py:17: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "/shared-libs/python3.7/py-core/lib/python3.7/site-packages/ipykernel_launcher.py:20: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n"
     ]
    },
    {
     "data": {
      "application/vnd.deepnote.dataframe.v2+json": {
       "column_count": 15,
       "columns": [
        {
         "dtype": "int64",
         "name": "Unnamed: 0",
         "stats": {
          "histogram": [
           {
            "bin_end": 9.8,
            "bin_start": 0,
            "count": 10
           },
           {
            "bin_end": 19.6,
            "bin_start": 9.8,
            "count": 10
           },
           {
            "bin_end": 29.400000000000002,
            "bin_start": 19.6,
            "count": 10
           },
           {
            "bin_end": 39.2,
            "bin_start": 29.400000000000002,
            "count": 10
           },
           {
            "bin_end": 49,
            "bin_start": 39.2,
            "count": 9
           },
           {
            "bin_end": 58.800000000000004,
            "bin_start": 49,
            "count": 10
           },
           {
            "bin_end": 68.60000000000001,
            "bin_start": 58.800000000000004,
            "count": 10
           },
           {
            "bin_end": 78.4,
            "bin_start": 68.60000000000001,
            "count": 10
           },
           {
            "bin_end": 88.2,
            "bin_start": 78.4,
            "count": 10
           },
           {
            "bin_end": 98,
            "bin_start": 88.2,
            "count": 10
           }
          ],
          "max": 98,
          "min": 0,
          "nan_count": 0,
          "unique_count": 99
         }
        },
        {
         "dtype": "object",
         "name": "Link",
         "stats": {
          "categories": [
           {
            "count": 1,
            "name": "https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird"
           },
           {
            "count": 1,
            "name": "https://www.goodreads.com/book/show/3.Harry_Potter_and_the_Sorcerer_s_Stone"
           },
           {
            "count": 97,
            "name": "97 others"
           }
          ],
          "nan_count": 0,
          "unique_count": 99
         }
        },
        {
         "dtype": "object",
         "name": "Title",
         "stats": {
          "categories": [
           {
            "count": 2,
            "name": "1984"
           },
           {
            "count": 1,
            "name": "To Kill a Mockingbird"
           },
           {
            "count": 96,
            "name": "96 others"
           }
          ],
          "nan_count": 0,
          "unique_count": 98
         }
        },
        {
         "dtype": "object",
         "name": "Author",
         "stats": {
          "categories": [
           {
            "count": 6,
            "name": "J.K. Rowling"
           },
           {
            "count": 4,
            "name": "J.R.R. Tolkien"
           },
           {
            "count": 89,
            "name": "73 others"
           }
          ],
          "nan_count": 0,
          "unique_count": 75
         }
        },
        {
         "dtype": "int64",
         "name": "Review Count",
         "stats": {
          "histogram": [
           {
            "bin_end": 17674.8,
            "bin_start": 140,
            "count": 31
           },
           {
            "bin_end": 35209.6,
            "bin_start": 17674.8,
            "count": 35
           },
           {
            "bin_end": 52744.399999999994,
            "bin_start": 35209.6,
            "count": 13
           },
           {
            "bin_end": 70279.2,
            "bin_start": 52744.399999999994,
            "count": 7
           },
           {
            "bin_end": 87814,
            "bin_start": 70279.2,
            "count": 8
           },
           {
            "bin_end": 105348.79999999999,
            "bin_start": 87814,
            "count": 1
           },
           {
            "bin_end": 122883.59999999999,
            "bin_start": 105348.79999999999,
            "count": 3
           },
           {
            "bin_end": 140418.4,
            "bin_start": 122883.59999999999,
            "count": 0
           },
           {
            "bin_end": 157953.19999999998,
            "bin_start": 140418.4,
            "count": 0
           },
           {
            "bin_end": 175488,
            "bin_start": 157953.19999999998,
            "count": 1
           }
          ],
          "max": 175488,
          "min": 140,
          "nan_count": 0,
          "unique_count": 98
         }
        },
        {
         "dtype": "int64",
         "name": "Rating Count",
         "stats": {
          "histogram": [
           {
            "bin_end": 753009.9,
            "bin_start": 2891,
            "count": 37
           },
           {
            "bin_end": 1503128.8,
            "bin_start": 753009.9,
            "count": 28
           },
           {
            "bin_end": 2253247.7,
            "bin_start": 1503128.8,
            "count": 13
           },
           {
            "bin_end": 3003366.6,
            "bin_start": 2253247.7,
            "count": 11
           },
           {
            "bin_end": 3753485.5,
            "bin_start": 3003366.6,
            "count": 5
           },
           {
            "bin_end": 4503604.4,
            "bin_start": 3753485.5,
            "count": 1
           },
           {
            "bin_end": 5253723.3,
            "bin_start": 4503604.4,
            "count": 2
           },
           {
            "bin_end": 6003842.2,
            "bin_start": 5253723.3,
            "count": 0
           },
           {
            "bin_end": 6753961.100000001,
            "bin_start": 6003842.2,
            "count": 1
           },
           {
            "bin_end": 7504080,
            "bin_start": 6753961.100000001,
            "count": 1
           }
          ],
          "max": 7504080,
          "min": 2891,
          "nan_count": 0,
          "unique_count": 98
         }
        },
        {
         "dtype": "float64",
         "name": "Rating Value",
         "stats": {
          "histogram": [
           {
            "bin_end": 3.54,
            "bin_start": 3.42,
            "count": 2
           },
           {
            "bin_end": 3.66,
            "bin_start": 3.54,
            "count": 1
           },
           {
            "bin_end": 3.7800000000000002,
            "bin_start": 3.66,
            "count": 4
           },
           {
            "bin_end": 3.9,
            "bin_start": 3.7800000000000002,
            "count": 11
           },
           {
            "bin_end": 4.02,
            "bin_start": 3.9,
            "count": 12
           },
           {
            "bin_end": 4.140000000000001,
            "bin_start": 4.02,
            "count": 18
           },
           {
            "bin_end": 4.26,
            "bin_start": 4.140000000000001,
            "count": 14
           },
           {
            "bin_end": 4.38,
            "bin_start": 4.26,
            "count": 26
           },
           {
            "bin_end": 4.5,
            "bin_start": 4.38,
            "count": 6
           },
           {
            "bin_end": 4.62,
            "bin_start": 4.5,
            "count": 5
           }
          ],
          "max": 4.62,
          "min": 3.42,
          "nan_count": 0,
          "unique_count": 56
         }
        },
        {
         "dtype": "float64",
         "name": "1st Pub",
         "stats": {
          "histogram": [
           {
            "bin_end": -519.3,
            "bin_start": -800,
            "count": 1
           },
           {
            "bin_end": -238.60000000000002,
            "bin_start": -519.3,
            "count": 0
           },
           {
            "bin_end": 42.09999999999991,
            "bin_start": -238.60000000000002,
            "count": 0
           },
           {
            "bin_end": 322.79999999999995,
            "bin_start": 42.09999999999991,
            "count": 0
           },
           {
            "bin_end": 603.5,
            "bin_start": 322.79999999999995,
            "count": 0
           },
           {
            "bin_end": 884.1999999999998,
            "bin_start": 603.5,
            "count": 0
           },
           {
            "bin_end": 1164.8999999999999,
            "bin_start": 884.1999999999998,
            "count": 0
           },
           {
            "bin_end": 1445.6,
            "bin_start": 1164.8999999999999,
            "count": 0
           },
           {
            "bin_end": 1726.2999999999997,
            "bin_start": 1445.6,
            "count": 5
           },
           {
            "bin_end": 2007,
            "bin_start": 1726.2999999999997,
            "count": 87
           }
          ],
          "max": 2007,
          "min": -800,
          "nan_count": 6,
          "unique_count": 73
         }
        },
        {
         "dtype": "int64",
         "name": "series",
         "stats": {
          "histogram": [
           {
            "bin_end": 0.1,
            "bin_start": 0,
            "count": 66
           },
           {
            "bin_end": 0.2,
            "bin_start": 0.1,
            "count": 0
           },
           {
            "bin_end": 0.30000000000000004,
            "bin_start": 0.2,
            "count": 0
           },
           {
            "bin_end": 0.4,
            "bin_start": 0.30000000000000004,
            "count": 0
           },
           {
            "bin_end": 0.5,
            "bin_start": 0.4,
            "count": 0
           },
           {
            "bin_end": 0.6000000000000001,
            "bin_start": 0.5,
            "count": 0
           },
           {
            "bin_end": 0.7000000000000001,
            "bin_start": 0.6000000000000001,
            "count": 0
           },
           {
            "bin_end": 0.8,
            "bin_start": 0.7000000000000001,
            "count": 0
           },
           {
            "bin_end": 0.9,
            "bin_start": 0.8,
            "count": 0
           },
           {
            "bin_end": 1,
            "bin_start": 0.9,
            "count": 33
           }
          ],
          "max": 1,
          "min": 0,
          "nan_count": 0,
          "unique_count": 2
         }
        },
        {
         "dtype": "object",
         "name": "Genres",
         "stats": {
          "categories": [
           {
            "count": 14,
            "name": "['Classics', 'Fiction', 'Historical']"
           },
           {
            "count": 7,
            "name": "['Classics', 'Fiction', 'Science Fiction']"
           },
           {
            "count": 78,
            "name": "44 others"
           }
          ],
          "nan_count": 0,
          "unique_count": 46
         }
        },
        {
         "dtype": "object",
         "name": "Awards",
         "stats": {
          "categories": [
           {
            "count": 40,
            "name": "[]"
           },
           {
            "count": 2,
            "name": "['Prometheus Hall of Fame Award (1984)', 'Locus Award Nominee for All-Time Best Science Fiction Novel (1987)']"
           },
           {
            "count": 57,
            "name": "57 others"
           }
          ],
          "nan_count": 0,
          "unique_count": 59
         }
        },
        {
         "dtype": "int64",
         "name": "N pag",
         "stats": {
          "histogram": [
           {
            "bin_end": 298.8,
            "bin_start": 32,
            "count": 42
           },
           {
            "bin_end": 565.6,
            "bin_start": 298.8,
            "count": 38
           },
           {
            "bin_end": 832.4000000000001,
            "bin_start": 565.6,
            "count": 8
           },
           {
            "bin_end": 1099.2,
            "bin_start": 832.4000000000001,
            "count": 4
           },
           {
            "bin_end": 1366,
            "bin_start": 1099.2,
            "count": 3
           },
           {
            "bin_end": 1632.8000000000002,
            "bin_start": 1366,
            "count": 3
           },
           {
            "bin_end": 1899.6000000000001,
            "bin_start": 1632.8000000000002,
            "count": 0
           },
           {
            "bin_end": 2166.4,
            "bin_start": 1899.6000000000001,
            "count": 0
           },
           {
            "bin_end": 2433.2000000000003,
            "bin_start": 2166.4,
            "count": 0
           },
           {
            "bin_end": 2700,
            "bin_start": 2433.2000000000003,
            "count": 1
           }
          ],
          "max": 2700,
          "min": 32,
          "nan_count": 0,
          "unique_count": 93
         }
        },
        {
         "dtype": "int64",
         "name": "award_number",
         "stats": {
          "histogram": [
           {
            "bin_end": 5,
            "bin_start": 1,
            "count": 80
           },
           {
            "bin_end": 9,
            "bin_start": 5,
            "count": 9
           },
           {
            "bin_end": 13,
            "bin_start": 9,
            "count": 3
           },
           {
            "bin_end": 17,
            "bin_start": 13,
            "count": 2
           },
           {
            "bin_end": 21,
            "bin_start": 17,
            "count": 1
           },
           {
            "bin_end": 25,
            "bin_start": 21,
            "count": 1
           },
           {
            "bin_end": 29,
            "bin_start": 25,
            "count": 2
           },
           {
            "bin_end": 33,
            "bin_start": 29,
            "count": 0
           },
           {
            "bin_end": 37,
            "bin_start": 33,
            "count": 0
           },
           {
            "bin_end": 41,
            "bin_start": 37,
            "count": 1
           }
          ],
          "max": 41,
          "min": 1,
          "nan_count": 0,
          "unique_count": 16
         }
        },
        {
         "dtype": "float64",
         "name": "mean_norm_ratings",
         "stats": {
          "histogram": [
           {
            "bin_end": -34.325757575757535,
            "bin_start": -43.325757575757535,
            "count": 2
           },
           {
            "bin_end": -25.325757575757535,
            "bin_start": -34.325757575757535,
            "count": 1
           },
           {
            "bin_end": -16.325757575757535,
            "bin_start": -25.325757575757535,
            "count": 4
           },
           {
            "bin_end": -7.325757575757535,
            "bin_start": -16.325757575757535,
            "count": 11
           },
           {
            "bin_end": 1.6742424242424647,
            "bin_start": -7.325757575757535,
            "count": 12
           },
           {
            "bin_end": 10.674242424242465,
            "bin_start": 1.6742424242424647,
            "count": 18
           },
           {
            "bin_end": 19.674242424242465,
            "bin_start": 10.674242424242465,
            "count": 17
           },
           {
            "bin_end": 28.674242424242465,
            "bin_start": 19.674242424242465,
            "count": 25
           },
           {
            "bin_end": 37.674242424242465,
            "bin_start": 28.674242424242465,
            "count": 5
           },
           {
            "bin_end": 46.674242424242465,
            "bin_start": 37.674242424242465,
            "count": 4
           }
          ],
          "max": 46.674242424242465,
          "min": -43.325757575757535,
          "nan_count": 0,
          "unique_count": 56
         }
        },
        {
         "dtype": "float64",
         "name": "min_max",
         "stats": {
          "histogram": [
           {
            "bin_end": 19,
            "bin_start": 10,
            "count": 2
           },
           {
            "bin_end": 28,
            "bin_start": 19,
            "count": 1
           },
           {
            "bin_end": 37,
            "bin_start": 28,
            "count": 4
           },
           {
            "bin_end": 46,
            "bin_start": 37,
            "count": 11
           },
           {
            "bin_end": 55,
            "bin_start": 46,
            "count": 12
           },
           {
            "bin_end": 64,
            "bin_start": 55,
            "count": 18
           },
           {
            "bin_end": 73,
            "bin_start": 64,
            "count": 17
           },
           {
            "bin_end": 82,
            "bin_start": 73,
            "count": 25
           },
           {
            "bin_end": 91,
            "bin_start": 82,
            "count": 5
           },
           {
            "bin_end": 100,
            "bin_start": 91,
            "count": 4
           }
          ],
          "max": 100,
          "min": 10,
          "nan_count": 0,
          "unique_count": 56
         }
        },
        {
         "dtype": "int64",
         "name": "_deepnote_index_column"
        }
       ],
       "row_count": 99,
       "rows_bottom": [
        {
         "1st Pub": "1877.0",
         "Author": "Leo Tolstoy",
         "Awards": "['PEN Translation Prize for Richard Pevear & Larissa Volokhonsky (2002)']",
         "Genres": "['Fiction', 'Romance', 'Cultural']",
         "Link": "https://www.goodreads.com/book/show/15823480-anna-karenina",
         "N pag": 964,
         "Rating Count": 696076,
         "Rating Value": 4.06,
         "Review Count": 25809,
         "Title": "Anna Karenina",
         "Unnamed: 0": 66,
         "_deepnote_index_column": 66,
         "award_number": 1,
         "mean_norm_ratings": 4.674242424242428,
         "min_max": 57.99999999999997,
         "series": 0
        },
        {
         "1st Pub": "1959.0",
         "Author": "Daniel Keyes",
         "Awards": "['Hugo Award Nominee for Best Novel (1967)', 'Nebula Award for Best Novel (tie) (1966)', 'Locus Award Nominee for All-Time Best Novel (36th in poll) (1975)']",
         "Genres": "['Fiction', 'Classics', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/35031085-frankenstein",
         "N pag": 216,
         "Rating Count": 505489,
         "Rating Value": 4.15,
         "Review Count": 20290,
         "Title": "Flowers for Algernon",
         "Unnamed: 0": 67,
         "_deepnote_index_column": 67,
         "award_number": 3,
         "mean_norm_ratings": 11.424242424242482,
         "min_max": 64.75000000000003,
         "series": 0
        },
        {
         "1st Pub": "1818.0",
         "Author": "Mary Wollstonecraft Shelley",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Horror']",
         "Link": "https://www.goodreads.com/book/show/36576608-flowers-for-algernon",
         "N pag": 288,
         "Rating Count": 1219362,
         "Rating Value": 3.82,
         "Review Count": 36399,
         "Title": "Frankenstein: The 1818 Text",
         "Unnamed: 0": 68,
         "_deepnote_index_column": 68,
         "award_number": 1,
         "mean_norm_ratings": -13.32575757575755,
         "min_max": 39.999999999999986,
         "series": 0
        },
        {
         "1st Pub": "1926.0",
         "Author": "A.A. Milne",
         "Awards": "[]",
         "Genres": "['Classics', 'Childrens', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/38447.The_Handmaid_s_Tale",
         "N pag": 145,
         "Rating Count": 287084,
         "Rating Value": 4.31,
         "Review Count": 5093,
         "Title": "Winnie-the-Pooh",
         "Unnamed: 0": 69,
         "_deepnote_index_column": 69,
         "award_number": 1,
         "mean_norm_ratings": 23.42424242424243,
         "min_max": 76.74999999999996,
         "series": 1
        },
        {
         "1st Pub": "1985.0",
         "Author": "Margaret Atwood",
         "Awards": "['Booker Prize Nominee (1986)', 'Nebula Award Nominee for Best Novel (1986)', 'Locus Award Nominee for Best SF Novel (1987)', 'Arthur C. Clarke Award (1987)', 'Audie Award for Fiction (2013)', 'Los Angeles Times Book Prize for Fiction (1986)', 'Prometheus Award Nominee for Best Novel (1987)', 'James Tiptree Jr. Award Nominee for Retrospective (1995)', \"Governor General's Literary Awards / Prix littéraires du Gouverneur général for Fiction (1985)\", 'SF Chronicle Award Nominee for Novel (1987)', \"Commonwealth Writers' Prize Nominee for Best Book in Caribbean and Canada (1987)\", 'CBC Canada Reads Nominee (2002)', 'Metų verstinė knyga Nominee (2012)']",
         "Genres": "['Fiction', 'Classics', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/99107.Winnie_the_Pooh",
         "N pag": 314,
         "Rating Count": 1557874,
         "Rating Value": 4.12,
         "Review Count": 74553,
         "Title": "The Handmaid's Tale",
         "Unnamed: 0": 70,
         "_deepnote_index_column": 70,
         "award_number": 13,
         "mean_norm_ratings": 9.174242424242465,
         "min_max": 62.5,
         "series": 1
        },
        {
         "1st Pub": "1997.0",
         "Author": "Mitch Albom",
         "Awards": "[]",
         "Genres": "['Nonfiction', 'Autobiography', 'Memoir']",
         "Link": "https://www.goodreads.com/book/show/6900.Tuesdays_with_Morrie",
         "N pag": 210,
         "Rating Count": 818466,
         "Rating Value": 4.12,
         "Review Count": 27468,
         "Title": "Tuesdays with Morrie",
         "Unnamed: 0": 71,
         "_deepnote_index_column": 71,
         "award_number": 1,
         "mean_norm_ratings": 9.174242424242465,
         "min_max": 62.5,
         "series": 0
        },
        {
         "1st Pub": "1954.0",
         "Author": "J.R.R. Tolkien",
         "Awards": "['Publieksprijs voor het Nederlandse Boek Nominee (2002)']",
         "Genres": "['Fantasy', 'Classics', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/3263607-the-fellowship-of-the-ring",
         "N pag": 527,
         "Rating Count": 2441028,
         "Rating Value": 4.37,
         "Review Count": 24800,
         "Title": "The Fellowship of the Ring",
         "Unnamed: 0": 72,
         "_deepnote_index_column": 72,
         "award_number": 1,
         "mean_norm_ratings": 27.924242424242465,
         "min_max": 81.25,
         "series": 1
        },
        {
         "1st Pub": "1969.0",
         "Author": "Kurt Vonnegut Jr.",
         "Awards": "['Hugo Award Nominee for Best SF Novel (1970)', 'Nebula Award Nominee for Best Novel (1969)', 'National Book Award Finalist for Fiction (1970)', \"Chicago Publishers' Award (1970)\"]",
         "Genres": "['Classics', 'Fiction', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/4981.Slaughterhouse_Five",
         "N pag": 275,
         "Rating Count": 1173167,
         "Rating Value": 4.08,
         "Review Count": 28430,
         "Title": "Slaughterhouse-Five",
         "Unnamed: 0": 73,
         "_deepnote_index_column": 73,
         "award_number": 4,
         "mean_norm_ratings": 6.174242424242463,
         "min_max": 59.50000000000001,
         "series": 0
        },
        {
         "1st Pub": "1961.0",
         "Author": "Joseph Heller",
         "Awards": "['National Book Award Finalist for Fiction (1962)']",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/168668.Catch_22",
         "N pag": 453,
         "Rating Count": 745469,
         "Rating Value": 3.98,
         "Review Count": 19026,
         "Title": "Catch-22",
         "Unnamed: 0": 74,
         "_deepnote_index_column": 74,
         "award_number": 1,
         "mean_norm_ratings": -1.3257575757575424,
         "min_max": 51.99999999999999,
         "series": 1
        },
        {
         "1st Pub": "1952.0",
         "Author": "Ernest Hemingway",
         "Awards": "['Pulitzer Prize for Fiction (1953)', 'Premio Bancarella (1953)', 'National Book Award Finalist for Fiction (1953)']",
         "Genres": "['Classics', 'Fiction', 'Literature']",
         "Link": "https://www.goodreads.com/book/show/2165.The_Old_Man_and_the_Sea",
         "N pag": 96,
         "Rating Count": 878824,
         "Rating Value": 3.79,
         "Review Count": 26865,
         "Title": "The Old Man and the Sea",
         "Unnamed: 0": 75,
         "_deepnote_index_column": 75,
         "award_number": 3,
         "mean_norm_ratings": -15.575757575757539,
         "min_max": 37.75000000000001,
         "series": 0
        },
        {
         "1st Pub": "1850.0",
         "Author": "Nathaniel Hawthorne",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/12296.The_Scarlet_Letter",
         "N pag": 279,
         "Rating Count": 728584,
         "Rating Value": 3.42,
         "Review Count": 15257,
         "Title": "The Scarlet Letter",
         "Unnamed: 0": 76,
         "_deepnote_index_column": 76,
         "award_number": 1,
         "mean_norm_ratings": -43.325757575757535,
         "min_max": 10,
         "series": 0
        },
        {
         "1st Pub": "1606.0",
         "Author": "William Shakespeare",
         "Awards": "[]",
         "Genres": "['Classics', 'Plays', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/8852.Macbeth",
         "N pag": 249,
         "Rating Count": 703961,
         "Rating Value": 3.91,
         "Review Count": 11922,
         "Title": "Macbeth",
         "Unnamed: 0": 77,
         "_deepnote_index_column": 77,
         "award_number": 1,
         "mean_norm_ratings": -6.575757575757528,
         "min_max": 46.75000000000001,
         "series": 0
        },
        {
         "1st Pub": "2005.0",
         "Author": "Stephenie Meyer",
         "Awards": "['Georgia Peach Book Award (2007)', 'Buxtehuder Bulle (2006)', 'Kentucky Bluegrass Award for 9-12 (2007)', 'Prijs van de Kinder- en Jeugdjury Vlaanderen (2008)', 'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2009)', \"West Australian Young Readers' Book Award (WAYRBA) for Older Readers (2008)\", 'Garden State Book Award for Fiction (Grades 9-12) (2008)', 'South Carolina Book Award for Young Adult Book Award (2008)', 'Grand Canyon Reader Award for Teen Book (2008)', 'Maryland Black-Eyed Susan Book Award for High School (2008)', 'Golden Sower Award for Young Adult (2009)', \"Nevada Young Readers' Award for Young Adult Category  (2007)\", \"The Flume: New Hampshire Teen Reader's Choice Award (2007)\", \"Pennsylvania Young Readers' Choice Award for Young Adult (2009)\", 'Rhode Island Teen Book Award (2007)', 'Evergreen Teen Book Award (2008)', 'Michigan Library Association Thumbs Up! Award Nominee (2006)', 'Teen Read Award Nominee for Best All-Time-Fave (2010)', 'Deutscher Jugendliteraturpreis Nominee for Preis der Jugendjury (2007)', 'Iowa High School Book Award (2008)', 'Eliot Rosewater Indiana High School Book Award (2008)', 'Lincoln Award (2008)', 'Literaturpreis der Jury der jungen Leser for Cover (2007)', 'Prix Et-lisez-moi (2008)', 'Missouri Gateway Readers Award (2008)']",
         "Genres": "['Young Adult', 'Fantasy', 'Romance']",
         "Link": "https://www.goodreads.com/book/show/41865.Twilight",
         "N pag": 501,
         "Rating Count": 5205621,
         "Rating Value": 3.61,
         "Review Count": 107225,
         "Title": "Twilight",
         "Unnamed: 0": 78,
         "_deepnote_index_column": 78,
         "award_number": 25,
         "mean_norm_ratings": -29.07575757575755,
         "min_max": 24.249999999999993,
         "series": 1
        },
        {
         "1st Pub": "2003.0",
         "Author": "Audrey Niffenegger",
         "Awards": "['Arthur C. Clarke Award Nominee (2005)', 'Orange Prize Nominee for Fiction Longlist (2004)', 'British Book Award (2006)', 'John W. Campbell Memorial Award Nominee for Best Science Fiction Novel (2005)', 'Exclusive Books Boeke Prize (2005)', 'ALA Alex Award (2004)']",
         "Genres": "['Fiction', 'Romance', 'Fantasy']",
         "Link": "https://www.goodreads.com/book/show/7604.Lolita",
         "N pag": 500,
         "Rating Count": 1619557,
         "Rating Value": 3.98,
         "Review Count": 47975,
         "Title": "The Time Traveler's Wife",
         "Unnamed: 0": 79,
         "_deepnote_index_column": 79,
         "award_number": 6,
         "mean_norm_ratings": -1.3257575757575424,
         "min_max": 51.99999999999999,
         "series": 0
        },
        {
         "1st Pub": "1922.0",
         "Author": "Hermann Hesse",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Philosophy']",
         "Link": "https://www.goodreads.com/book/show/18619684-the-time-traveler-s-wife",
         "N pag": 152,
         "Rating Count": 613891,
         "Rating Value": 4.04,
         "Review Count": 18781,
         "Title": "Siddhartha",
         "Unnamed: 0": 80,
         "_deepnote_index_column": 80,
         "award_number": 1,
         "mean_norm_ratings": 3.1742424242424594,
         "min_max": 56.50000000000001,
         "series": 0
        },
        {
         "1st Pub": "1915.0",
         "Author": "Franz Kafka",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Fantasy']",
         "Link": "https://www.goodreads.com/book/show/52036.Siddhartha",
         "N pag": 201,
         "Rating Count": 693081,
         "Rating Value": 3.83,
         "Review Count": 19726,
         "Title": "The Metamorphosis",
         "Unnamed: 0": 81,
         "_deepnote_index_column": 81,
         "award_number": 1,
         "mean_norm_ratings": -12.575757575757532,
         "min_max": 40.75000000000001,
         "series": 0
        },
        {
         "1st Pub": "1942.0",
         "Author": "Albert Camus",
         "Awards": "['PEN Translation Prize for Matthew Ward (1989)']",
         "Genres": "['Classics', 'Fiction', 'Philosophy']",
         "Link": "https://www.goodreads.com/book/show/485894.The_Metamorphosis",
         "N pag": 123,
         "Rating Count": 755360,
         "Rating Value": 3.99,
         "Review Count": 25275,
         "Title": "The Stranger",
         "Unnamed: 0": 82,
         "_deepnote_index_column": 82,
         "award_number": 1,
         "mean_norm_ratings": -0.5757575757575264,
         "min_max": 52.750000000000014,
         "series": 0
        },
        {
         "1st Pub": "1947.0",
         "Author": "Margaret Wise Brown",
         "Awards": "[]",
         "Genres": "['Childrens', 'Childrens', 'Picture Books']",
         "Link": "https://www.goodreads.com/book/show/49552.The_Stranger",
         "N pag": 32,
         "Rating Count": 320375,
         "Rating Value": 4.28,
         "Review Count": 6076,
         "Title": "Goodnight Moon",
         "Unnamed: 0": 83,
         "_deepnote_index_column": 83,
         "award_number": 1,
         "mean_norm_ratings": 21.174242424242472,
         "min_max": 74.50000000000001,
         "series": 1
        },
        {
         "1st Pub": "1943.0",
         "Author": "Betty  Smith",
         "Awards": "['Audie Award for Classic (2002)']",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/32929.Goodnight_Moon",
         "N pag": 496,
         "Rating Count": 400608,
         "Rating Value": 4.27,
         "Review Count": 21559,
         "Title": "A Tree Grows in Brooklyn",
         "Unnamed: 0": 84,
         "_deepnote_index_column": 84,
         "award_number": 1,
         "mean_norm_ratings": 20.424242424242422,
         "min_max": 73.74999999999997,
         "series": 0
        },
        {
         "1st Pub": "1865.0",
         "Author": "Leo Tolstoy",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/14891.A_Tree_Grows_in_Brooklyn",
         "N pag": 1392,
         "Rating Count": 275666,
         "Rating Value": 4.12,
         "Review Count": 12316,
         "Title": "War and Peace",
         "Unnamed: 0": 85,
         "_deepnote_index_column": 85,
         "award_number": 1,
         "mean_norm_ratings": 9.174242424242465,
         "min_max": 62.5,
         "series": 1
        },
        {
         "1st Pub": "1998.0",
         "Author": "J.K. Rowling",
         "Awards": "[\"Mythopoeic Fantasy Award for Children's Literature (2008)\", 'British Book Award (1999)', 'Prijs van de Jonge Jury (2002)', 'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2006)', 'Colorado Blue Spruce Young Adult Book Award (2008)', 'Golden Archer Award for Middle/Junior High (2008)', 'Nestlé Smarties Book Prize for 9–11 years (1998)']",
         "Genres": "['Fantasy', 'Young Adult', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/656.War_and_Peace",
         "N pag": 341,
         "Rating Count": 2904901,
         "Rating Value": 4.43,
         "Review Count": 56503,
         "Title": "Harry Potter and the Chamber of Secrets",
         "Unnamed: 0": 86,
         "_deepnote_index_column": 86,
         "award_number": 7,
         "mean_norm_ratings": 32.424242424242436,
         "min_max": 85.74999999999997,
         "series": 1
        },
        {
         "1st Pub": "1971.0",
         "Author": "Laura Ingalls Wilder",
         "Awards": "[]",
         "Genres": "['Classics', 'Historical', 'Historical Fiction']",
         "Link": "https://www.goodreads.com/book/show/15881.Harry_Potter_and_the_Chamber_of_Secrets",
         "N pag": 2700,
         "Rating Count": 144541,
         "Rating Value": 4.34,
         "Review Count": 2264,
         "Title": "The Little House Collection",
         "Unnamed: 0": 87,
         "_deepnote_index_column": 87,
         "award_number": 1,
         "mean_norm_ratings": 25.674242424242443,
         "min_max": 78.99999999999999,
         "series": 1
        },
        {
         "1st Pub": "1962.0",
         "Author": "Anthony Burgess",
         "Awards": "['Prometheus Hall of Fame Award (2008)']",
         "Genres": "['Classics', 'Fiction', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/114345.The_Little_House_Collection",
         "N pag": 213,
         "Rating Count": 623913,
         "Rating Value": 3.99,
         "Review Count": 14628,
         "Title": "A Clockwork Orange",
         "Unnamed: 0": 88,
         "_deepnote_index_column": 88,
         "award_number": 1,
         "mean_norm_ratings": -0.5757575757575264,
         "min_max": 52.750000000000014,
         "series": 0
        },
        {
         "1st Pub": "1929.0",
         "Author": "Erich Maria Remarque",
         "Awards": "['Luisterboek Award Nominee (2015)']",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/41817486-a-clockwork-orange",
         "N pag": 296,
         "Rating Count": 367338,
         "Rating Value": 3.99,
         "Review Count": 11116,
         "Title": "All Quiet on the Western Front",
         "Unnamed: 0": 89,
         "_deepnote_index_column": 89,
         "award_number": 1,
         "mean_norm_ratings": -0.5757575757575264,
         "min_max": 52.750000000000014,
         "series": 1
        },
        {
         "1st Pub": "1978.0",
         "Author": "Stephen King",
         "Awards": "['Locus Award Nominee for Best SF Novel (1979)', 'World Fantasy Award Nominee for Best Novel (1979)', 'Gandalf Award Nominee (1979)', 'Balrog Award Nominee for Best Novel (1979) (1980)']",
         "Genres": "['Horror', 'Fiction', 'Fantasy']",
         "Link": "https://www.goodreads.com/book/show/355697.All_Quiet_on_the_Western_Front",
         "N pag": 1152,
         "Rating Count": 646373,
         "Rating Value": 4.34,
         "Review Count": 22440,
         "Title": "The Stand",
         "Unnamed: 0": 90,
         "_deepnote_index_column": 90,
         "award_number": 4,
         "mean_norm_ratings": 25.674242424242443,
         "min_max": 78.99999999999999,
         "series": 0
        },
        {
         "1st Pub": "1851.0",
         "Author": "Harriet Beecher Stowe",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/46787.Uncle_Tom_s_Cabin",
         "N pag": 438,
         "Rating Count": 204435,
         "Rating Value": 3.88,
         "Review Count": 8146,
         "Title": "Uncle Tom's Cabin",
         "Unnamed: 0": 91,
         "_deepnote_index_column": 91,
         "award_number": 1,
         "mean_norm_ratings": -8.82575757575755,
         "min_max": 44.49999999999999,
         "series": 0
        },
        {
         "1st Pub": "1605.0",
         "Author": "Miguel de Cervantes Saavedra",
         "Awards": "['Will Eisner Comic Industry Awards Nominee for Best Adaptation from Another Medium & Best Humor Publication (2014)', 'Βραβείο Λογοτεχνικής Μετάφρασης ΕΚΕΜΕΛ for Ισπανόφωνη Λογοτεχνία (2010)', 'Premio de traducción literaria Valle Inclán for John Rutherford (2002)']",
         "Genres": "['Classics', 'Fiction', 'Literature']",
         "Link": "https://www.goodreads.com/book/show/3836.Don_Quixote",
         "N pag": 1023,
         "Rating Count": 221258,
         "Rating Value": 3.88,
         "Review Count": 8660,
         "Title": "Don Quixote",
         "Unnamed: 0": 92,
         "_deepnote_index_column": 92,
         "award_number": 3,
         "mean_norm_ratings": -8.82575757575755,
         "min_max": 44.49999999999999,
         "series": 0
        },
        {
         "1st Pub": "1957.0",
         "Author": "Ayn Rand",
         "Awards": "['Prometheus Hall of Fame Award (1983)', 'National Book Award Finalist for Fiction (1958)']",
         "Genres": "['Fiction', 'Classics', 'Philosophy']",
         "Link": "https://www.goodreads.com/book/show/646462._",
         "N pag": 1078,
         "Rating Count": 361725,
         "Rating Value": 3.69,
         "Review Count": 17828,
         "Title": "Atlas Shrugged",
         "Unnamed: 0": 93,
         "_deepnote_index_column": 93,
         "award_number": 2,
         "mean_norm_ratings": -23.075757575757542,
         "min_max": 30.249999999999996,
         "series": 0
        },
        {
         "1st Pub": "nan",
         "Author": "Anonymous",
         "Awards": "[]",
         "Genres": "['Religion', 'Religion', 'Islam']",
         "Link": "https://www.goodreads.com/book/show/662.Atlas_Shrugged",
         "N pag": 604,
         "Rating Count": 59042,
         "Rating Value": 4.35,
         "Review Count": 3146,
         "Title": "القرآن الكريم",
         "Unnamed: 0": 94,
         "_deepnote_index_column": 94,
         "award_number": 1,
         "mean_norm_ratings": 26.42424242424243,
         "min_max": 79.74999999999997,
         "series": 0
        },
        {
         "1st Pub": "1830.0",
         "Author": "Anonymous",
         "Awards": "[]",
         "Genres": "['Religion', 'Nonfiction', 'Christianity']",
         "Link": "https://www.goodreads.com/book/show/4934.The_Brothers_Karamazov",
         "N pag": 531,
         "Rating Count": 77516,
         "Rating Value": 4.32,
         "Review Count": 6021,
         "Title": "The Book of Mormon: Another Testament of Jesus Christ",
         "Unnamed: 0": 95,
         "_deepnote_index_column": 95,
         "award_number": 1,
         "mean_norm_ratings": 24.17424242424248,
         "min_max": 77.50000000000001,
         "series": 0
        },
        {
         "1st Pub": "1879.0",
         "Author": "Fyodor Dostoyevsky",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Cultural']",
         "Link": "https://www.goodreads.com/book/show/323355.The_Book_of_Mormon",
         "N pag": 796,
         "Rating Count": 255569,
         "Rating Value": 4.32,
         "Review Count": 11994,
         "Title": "The Brothers Karamazov",
         "Unnamed: 0": 96,
         "_deepnote_index_column": 96,
         "award_number": 1,
         "mean_norm_ratings": 24.17424242424248,
         "min_max": 77.50000000000001,
         "series": 1
        },
        {
         "1st Pub": "1998.0",
         "Author": "Barbara Kingsolver",
         "Awards": "['Pulitzer Prize Nominee for Fiction (1999)', 'Orange Prize Nominee for Fiction Shortlist (1999)', 'Book Sense Book of the Year Award for Adult (2000)', 'PEN/Faulkner Award for Fiction Nominee (1999)', 'Independent Publisher Book Award (IPPY) for Audio Fiction - Unabridged (1999)', 'Exclusive Books Boeke Prize (2000)', 'Puddly Award for Novel (2001)', 'International Dublin Literary Award Nominee (2000)']",
         "Genres": "['Fiction', 'Historical', 'Historical Fiction']",
         "Link": "https://www.goodreads.com/book/show/7244.The_Poisonwood_Bible",
         "N pag": 546,
         "Rating Count": 672550,
         "Rating Value": 4.07,
         "Review Count": 23753,
         "Title": "The Poisonwood Bible",
         "Unnamed: 0": 97,
         "_deepnote_index_column": 97,
         "award_number": 8,
         "mean_norm_ratings": 5.424242424242479,
         "min_max": 58.750000000000014,
         "series": 0
        },
        {
         "1st Pub": "1851.0",
         "Author": "Herman Melville",
         "Awards": "['Audie Award for Solo Narration - Male (2006)', 'Премія імені Максима Рильського (1991)']",
         "Genres": "['Classics', 'Fiction', 'Literature']",
         "Link": "https://www.goodreads.com/book/show/153747.Moby_Dick_or_the_Whale",
         "N pag": 654,
         "Rating Count": 491913,
         "Rating Value": 3.51,
         "Review Count": 16621,
         "Title": "Moby-Dick or, the Whale",
         "Unnamed: 0": 98,
         "_deepnote_index_column": 98,
         "award_number": 2,
         "mean_norm_ratings": -36.57575757575755,
         "min_max": 16.74999999999999,
         "series": 0
        }
       ],
       "rows_top": [
        {
         "1st Pub": "1960.0",
         "Author": "Harper Lee",
         "Awards": "['Pulitzer Prize for Fiction (1961)', 'Audie Award for Classic (2007)', 'National Book Award Finalist for Fiction (1961)', 'Alabama Author Award for Fiction (1961)']",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird",
         "N pag": 324,
         "Rating Count": 4747905,
         "Rating Value": 4.28,
         "Review Count": 95090,
         "Title": "To Kill a Mockingbird",
         "Unnamed: 0": 0,
         "_deepnote_index_column": 0,
         "award_number": 4,
         "mean_norm_ratings": 21.174242424242472,
         "min_max": 74.50000000000001,
         "series": 1
        },
        {
         "1st Pub": "1997.0",
         "Author": "J.K. Rowling",
         "Awards": "[\"Mythopoeic Fantasy Award for Children's Literature (2008)\", \"British Book Award for Children's Book of the Year (1998)\", 'Prijs van de Nederlandse Kinderjury for 6-9 jaar en 10-12 jaar (2002)', 'American Booksellers Book Of The Year  Award for Children (1999)', 'Audie Award (2000)', \"West Australian Young Readers' Book Award (WAYRBA) for Younger Readers (2000)\", 'South Carolina Book Award for Junior Book Award (2001)', 'Grand Canyon Reader Award for Teen Book (2000)', 'Charlotte Award (2000)', 'Nene Award (2000)', \"Massachusetts Children's Book Award (2000)\", 'Colorado Blue Spruce Young Adult Book Award (2001)', 'Blue Hen Book Award for Chapter Book (2001)', \"Nevada Young Readers' Award for Young Reader Category (2000)\", 'Golden Archer Award for Middle/Junior High (2000)', 'Indian Paintbrush Book Award (2000)', 'Hotze de Roosprijs (2002)', 'Nestlé Smarties Book Prize for 9–11 years (1997)', 'Eliot Rosewater Indiana High School Book Award (2001)', 'Kinderboekwinkelprijs (1999)', 'Parenting Book of the Year Award (1998)', 'North East Teenage Book Award (1999)', \"Specsavers National Book Award for Children's Book of the Year (1998)\", 'Washington State Sasquatch Award (2000)', 'Literaturpreis der Jury der jungen Leser for Kinderbuch (1999)', 'Carnegie Medal Nominee (1997)', \"Rebecca Caudill Young Readers' Book Award (2001)\", 'Premi Protagonista Jove for Categoria 12-13 anys (2000)']",
         "Genres": "['Fantasy', 'Fiction', 'Young Adult']",
         "Link": "https://www.goodreads.com/book/show/3.Harry_Potter_and_the_Sorcerer_s_Stone",
         "N pag": 309,
         "Rating Count": 7504080,
         "Rating Value": 4.48,
         "Review Count": 118948,
         "Title": "Harry Potter and the Sorcerer's Stone",
         "Unnamed: 0": 1,
         "_deepnote_index_column": 1,
         "award_number": 28,
         "mean_norm_ratings": 36.17424242424248,
         "min_max": 89.50000000000003,
         "series": 1
        },
        {
         "1st Pub": "1947.0",
         "Author": "Anne Frank",
         "Awards": "['Luisterboek Award Nominee (2008)']",
         "Genres": "['Nonfiction', 'Classics', 'History']",
         "Link": "https://www.goodreads.com/book/show/1885.Pride_and_Prejudice",
         "N pag": 283,
         "Rating Count": 2912898,
         "Rating Value": 4.16,
         "Review Count": 30804,
         "Title": "The Diary of a Young Girl",
         "Unnamed: 0": 2,
         "_deepnote_index_column": 2,
         "award_number": 1,
         "mean_norm_ratings": 12.174242424242468,
         "min_max": 65.50000000000001,
         "series": 0
        },
        {
         "1st Pub": "1813.0",
         "Author": "Jane Austen",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Romance']",
         "Link": "https://www.goodreads.com/book/show/48855.The_Diary_of_a_Young_Girl",
         "N pag": 279,
         "Rating Count": 3185479,
         "Rating Value": 4.27,
         "Review Count": 73295,
         "Title": "Pride and Prejudice",
         "Unnamed: 0": 3,
         "_deepnote_index_column": 3,
         "award_number": 1,
         "mean_norm_ratings": 20.424242424242422,
         "min_max": 73.74999999999997,
         "series": 0
        },
        {
         "1st Pub": "1943.0",
         "Author": "Antoine de Saint-Exupéry",
         "Awards": "['Retro Hugo Award for Best Novella (2019)']",
         "Genres": "['Classics', 'Fiction', 'Fantasy']",
         "Link": "https://www.goodreads.com/book/show/170448.Animal_Farm",
         "N pag": 93,
         "Rating Count": 1481259,
         "Rating Value": 4.31,
         "Review Count": 43183,
         "Title": "The Little Prince",
         "Unnamed: 0": 4,
         "_deepnote_index_column": 4,
         "award_number": 1,
         "mean_norm_ratings": 23.42424242424243,
         "min_max": 76.74999999999996,
         "series": 0
        },
        {
         "1st Pub": "1945.0",
         "Author": "George Orwell",
         "Awards": "['Prometheus Hall of Fame Award (2011)', 'Retro Hugo Award for Best Novella (1996)']",
         "Genres": "['Classics', 'Fiction', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/157993.The_Little_Prince",
         "N pag": 141,
         "Rating Count": 2909027,
         "Rating Value": 3.96,
         "Review Count": 60971,
         "Title": "Animal Farm",
         "Unnamed: 0": 5,
         "_deepnote_index_column": 5,
         "award_number": 2,
         "mean_norm_ratings": -2.825757575757546,
         "min_max": 50.49999999999999,
         "series": 0
        },
        {
         "1st Pub": "1951.0",
         "Author": "J.D. Salinger",
         "Awards": "['Teen Read Award Nominee for Best All-Time-Fave (2010)', 'National Book Award Finalist for Fiction (1952)']",
         "Genres": "['Classics', 'Fiction', 'Young Adult']",
         "Link": "https://www.goodreads.com/book/show/4671.The_Great_Gatsby",
         "N pag": 277,
         "Rating Count": 2856849,
         "Rating Value": 3.81,
         "Review Count": 60314,
         "Title": "The Catcher in the Rye",
         "Unnamed: 0": 6,
         "_deepnote_index_column": 6,
         "award_number": 2,
         "mean_norm_ratings": -14.075757575757539,
         "min_max": 39.25000000000001,
         "series": 0
        },
        {
         "1st Pub": "1925.0",
         "Author": "F. Scott Fitzgerald",
         "Awards": "['Grammy Award Nominee for Best Spoken Word Album (2003)', 'Long Island Reads (2002)']",
         "Genres": "['Classics', 'Fiction', 'Academic']",
         "Link": "https://www.goodreads.com/book/show/5107.The_Catcher_in_the_Rye",
         "N pag": 200,
         "Rating Count": 3977672,
         "Rating Value": 3.93,
         "Review Count": 71568,
         "Title": "The Great Gatsby",
         "Unnamed: 0": 7,
         "_deepnote_index_column": 7,
         "award_number": 2,
         "mean_norm_ratings": -5.07575757575753,
         "min_max": 48.250000000000014,
         "series": 0
        },
        {
         "1st Pub": "1955.0",
         "Author": "J.R.R. Tolkien",
         "Awards": "['Hugo Award Nominee for Best All-Time Series (1966)', 'Prometheus Hall of Fame Award (2009)', 'International Fantasy Award for Fiction (1957)', 'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2002)', 'Prix du Meilleur Livre Étranger for Roman (1972)', 'Nynorsk litteraturpris (2006)']",
         "Genres": "['Fantasy', 'Classics', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/33.The_Lord_of_the_Rings",
         "N pag": 1216,
         "Rating Count": 589544,
         "Rating Value": 4.5,
         "Review Count": 12043,
         "Title": "The Lord of the Rings",
         "Unnamed: 0": 8,
         "_deepnote_index_column": 8,
         "award_number": 6,
         "mean_norm_ratings": 37.67424242424245,
         "min_max": 90.99999999999999,
         "series": 1
        },
        {
         "1st Pub": "2005.0",
         "Author": "Markus Zusak",
         "Awards": "['National Jewish Book Award for Children’s and Young Adult Literature (2006)', \"Book Sense Book of the Year Award for Children's Literature (2007)\", 'Buxtehuder Bulle (2008)', 'Sydney Taylor Book Award for Teen Readers (2007)', 'Prijs van de Kinder- en Jeugdjury Vlaanderen (2009)', 'Michael L. Printz Award Nominee (2007)', 'Exclusive Books Boeke Prize (2007)', 'Rhode Island Teen Book Award Nominee (2008)', 'The Quill Award Nominee for Young Adult/Teen (2006)', 'Zilveren Zoen (2008)', 'Teen Read Award Nominee for Best All-Time-Fave (2010)', 'Deutscher Jugendliteraturpreis for Preis der Jugendjury (2009)', 'Association of Jewish Libraries for Teen Book Award (2006)', 'Lincoln Award Nominee (2010)', 'Australian Book Industry Award (ABIA) Nominee for Literary Fiction (2008)', 'Kathleen Mitchell Award', 'Ena Noel Award (2008)', 'Literaturpreis der Jury der jungen Leser for Jugendbuch (2009)', 'LovelyBooks Leserpreis for Allgemeine Literatur (2009)', 'Margaret A. Edwards Award (2014)']",
         "Genres": "['Historical', 'Historical Fiction', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/19063.The_Book_Thief",
         "N pag": 552,
         "Rating Count": 1941639,
         "Rating Value": 4.38,
         "Review Count": 116793,
         "Title": "The Book Thief",
         "Unnamed: 0": 9,
         "_deepnote_index_column": 9,
         "award_number": 20,
         "mean_norm_ratings": 28.674242424242447,
         "min_max": 81.99999999999999,
         "series": 0
        },
        {
         "1st Pub": "1847.0",
         "Author": "Charlotte Brontë",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Romance']",
         "Link": "https://www.goodreads.com/book/show/10210.Jane_Eyre",
         "N pag": 532,
         "Rating Count": 1698637,
         "Rating Value": 4.13,
         "Review Count": 45111,
         "Title": "Jane Eyre",
         "Unnamed: 0": 10,
         "_deepnote_index_column": 10,
         "award_number": 1,
         "mean_norm_ratings": 9.924242424242449,
         "min_max": 63.24999999999999,
         "series": 0
        },
        {
         "1st Pub": "1949.0",
         "Author": "George Orwell",
         "Awards": "['Prometheus Hall of Fame Award (1984)', 'Locus Award Nominee for All-Time Best Science Fiction Novel (1987)']",
         "Genres": "['Classics', 'Fiction', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/5470.1984",
         "N pag": 328,
         "Rating Count": 3362159,
         "Rating Value": 4.19,
         "Review Count": 75975,
         "Title": "1984",
         "Unnamed: 0": 11,
         "_deepnote_index_column": 11,
         "award_number": 2,
         "mean_norm_ratings": 14.424242424242486,
         "min_max": 67.75000000000003,
         "series": 0
        },
        {
         "1st Pub": "1954.0",
         "Author": "William Golding",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Young Adult']",
         "Link": "https://www.goodreads.com/book/show/11127.The_Chronicles_of_Narnia",
         "N pag": 182,
         "Rating Count": 2361640,
         "Rating Value": 3.69,
         "Review Count": 39807,
         "Title": "Lord of the Flies",
         "Unnamed: 0": 12,
         "_deepnote_index_column": 12,
         "award_number": 1,
         "mean_norm_ratings": -23.075757575757542,
         "min_max": 30.249999999999996,
         "series": 0
        },
        {
         "1st Pub": "1956.0",
         "Author": "C.S. Lewis",
         "Awards": "[]",
         "Genres": "['Fantasy', 'Classics', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/7624.Lord_of_the_Flies",
         "N pag": 767,
         "Rating Count": 545427,
         "Rating Value": 4.26,
         "Review Count": 10668,
         "Title": "The Chronicles of Narnia",
         "Unnamed: 0": 13,
         "_deepnote_index_column": 13,
         "award_number": 1,
         "mean_norm_ratings": 19.67424242424244,
         "min_max": 72.99999999999997,
         "series": 1
        },
        {
         "1st Pub": "nan",
         "Author": "J.K. Rowling",
         "Awards": "['Locus Award Nominee for Best Young Adult Novel (2008)', 'Odyssey Award Nominee (2008)', 'Audie Award (2008)', 'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2008)', 'Teen Read Award Nominee for Best All-Time-Fave (2010)', 'Puddly Award for Fiction (2008)', 'Andre Norton Award (2007)', 'Carnegie Medal Nominee (2008)']",
         "Genres": "['Fantasy', 'Young Adult', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/18135.Romeo_and_Juliet",
         "N pag": 759,
         "Rating Count": 2959099,
         "Rating Value": 4.62,
         "Review Count": 68439,
         "Title": "Harry Potter and the Deathly Hallows",
         "Unnamed: 0": 14,
         "_deepnote_index_column": 14,
         "award_number": 8,
         "mean_norm_ratings": 46.674242424242465,
         "min_max": 100,
         "series": 1
        },
        {
         "1st Pub": "1597.0",
         "Author": "William Shakespeare",
         "Awards": "[]",
         "Genres": "['Classics', 'Plays', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/136251.Harry_Potter_and_the_Deathly_Hallows",
         "N pag": 301,
         "Rating Count": 2135032,
         "Rating Value": 3.75,
         "Review Count": 20436,
         "Title": "Romeo and Juliet",
         "Unnamed: 0": 15,
         "_deepnote_index_column": 15,
         "award_number": 1,
         "mean_norm_ratings": -18.575757575757535,
         "min_max": 34.75,
         "series": 0
        },
        {
         "1st Pub": "2003.0",
         "Author": "Khaled Hosseini",
         "Awards": "['Borders Original Voices Award for Fiction (2003)', \"Humo's Gouden Bladwijzer (2008)\", 'Exclusive Books Boeke Prize (2004)', 'ALA Alex Award (2004)', 'Puddly Award for Fiction (2006)', 'Lincoln Award Nominee (2006)', 'Prix des libraires du Québec for Lauréats hors Québec (2006)', 'LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)']",
         "Genres": "['Fiction', 'Historical', 'Historical Fiction']",
         "Link": "https://www.goodreads.com/book/show/77203.The_Kite_Runner",
         "N pag": 371,
         "Rating Count": 2537928,
         "Rating Value": 4.31,
         "Review Count": 76661,
         "Title": "The Kite Runner",
         "Unnamed: 0": 16,
         "_deepnote_index_column": 16,
         "award_number": 8,
         "mean_norm_ratings": 23.42424242424243,
         "min_max": 76.74999999999996,
         "series": 0
        },
        {
         "1st Pub": "1993.0",
         "Author": "Lois Lowry",
         "Awards": "['Newbery Medal (1994)', \"Mythopoeic Fantasy Award Nominee for Children's Literature (1994)\", 'Golden Duck Award for Young Adult (Hal Clement Award) (1994)', 'Garden State Book Award for Teen Fiction Grades 6-8 (1996)', \"Buckeye Children's Book Award for Grade 6-8 (1997)\", 'Grand Canyon Reader Award for Teen Book (1995)', 'Maryland Black-Eyed Susan Book Award for Grade 6-9 (1995)', 'Golden Sower Award for Young Adult (1995)', \"Pennsylvania Young Readers' Choice Award for Grades 3-8 (1995)\", 'Soaring Eagle Book Award Nominee (1996)', \"Pacific Northwest Library Association Young Reader's Choice Award for Senior (1996)\", 'Boston Globe-Horn Book Award Nominee for Fiction (1993)', 'New Mexico Land of Enchantment Award (1997)', 'Eliot Rosewater Indiana High School Book Award (1997)', \"William Allen White Children's Book Award (1996)\", 'Wyoming Indian Paintbrush Nominee (1996)', \"NSK Neustadt Prize for Children's Literature Nominee (2013)\", 'Oklahoma Sequoyah Award for YA (1996)', \"Rebecca Caudill Young Readers' Book Award (1996)\", 'Hea Lasteraamat (2010)', 'Premi Protagonista Jove for Categoria 13-14 anys (2016)', 'Margaret A. Edwards Award (2007)']",
         "Genres": "['Young Adult', 'Fiction', 'Classics']",
         "Link": "https://www.goodreads.com/book/show/3636.The_Giver",
         "N pag": 208,
         "Rating Count": 1884995,
         "Rating Value": 4.13,
         "Review Count": 67042,
         "Title": "The Giver",
         "Unnamed: 0": 17,
         "_deepnote_index_column": 17,
         "award_number": 22,
         "mean_norm_ratings": 9.924242424242449,
         "min_max": 63.24999999999999,
         "series": 1
        },
        {
         "1st Pub": "1964.0",
         "Author": "Shel Silverstein",
         "Awards": "[]",
         "Genres": "['Childrens', 'Childrens', 'Picture Books']",
         "Link": "https://www.goodreads.com/book/show/370493.The_Giving_Tree",
         "N pag": 64,
         "Rating Count": 948299,
         "Rating Value": 4.37,
         "Review Count": 18545,
         "Title": "The Giving Tree",
         "Unnamed: 0": 18,
         "_deepnote_index_column": 18,
         "award_number": 1,
         "mean_norm_ratings": 27.924242424242465,
         "min_max": 81.25,
         "series": 0
        },
        {
         "1st Pub": "1952.0",
         "Author": "E.B. White",
         "Awards": "['Newbery Medal Nominee (1953)', \"George C. Stone Center for Children's Books Recognition of Merit Award (1970)\", 'Audie Award Nominee for Audiobook of the Year and Middle Grade (2020)', \"Massachusetts Children's Book Award (1984)\", 'Laura Ingalls Wilder Award (1970)']",
         "Genres": "['Classics', 'Childrens', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/24178.Charlotte_s_Web",
         "N pag": 184,
         "Rating Count": 1491548,
         "Rating Value": 4.17,
         "Review Count": 18993,
         "Title": "Charlotte's Web",
         "Unnamed: 0": 19,
         "_deepnote_index_column": 19,
         "award_number": 5,
         "mean_norm_ratings": 12.92424242424245,
         "min_max": 66.25,
         "series": 0
        },
        {
         "1st Pub": "1868.0",
         "Author": "Louisa May Alcott",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Historical']",
         "Link": "https://www.goodreads.com/book/show/2767052-the-hunger-games",
         "N pag": 449,
         "Rating Count": 1756339,
         "Rating Value": 4.1,
         "Review Count": 32972,
         "Title": "Little Women",
         "Unnamed: 0": 20,
         "_deepnote_index_column": 20,
         "award_number": 1,
         "mean_norm_ratings": 7.674242424242431,
         "min_max": 60.99999999999997,
         "series": 1
        },
        {
         "1st Pub": "nan",
         "Author": "Suzanne Collins",
         "Awards": "['Locus Award Nominee for Best Young Adult Book (2009)', 'Georgia Peach Book Award (2009)', 'Buxtehuder Bulle (2009)', 'Golden Duck Award for Young Adult (Hal Clement Award) (2009)', \"Grand Prix de l'Imaginaire Nominee for Roman jeunesse étranger (2010)\", 'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2012)', \"West Australian Young Readers' Book Award (WAYRBA) for Older Readers (2010)\", \"Red House Children's Book Award for Older Readers & Overall (2010)\", 'South Carolina Book Award for Junior and Young Adult Book (2011)', 'Charlotte Award (2010)', 'Colorado Blue Spruce Young Adult Book Award (2010)', 'Teen Buckeye Book Award (2009)', \"Pennsylvania Young Readers' Choice Award for Young Adults (2010)\", 'Rhode Island Teen Book Award (2010)', \"Dorothy Canfield Fisher Children's Book Award (2010)\", 'Evergreen Teen Book Award (2011)', 'Soaring Eagle Book Award (2009)', 'Milwaukee County Teen Book Award Nominee (2010)', 'Sakura Medal for Middle School Book (2010)', 'Michigan Library Association Thumbs Up! Award (2009)', 'Florida Teens Read (2009)', 'Deutscher Jugendliteraturpreis for Preis der Jugendjury (2010)', 'Iowa High School Book Award (2011)', 'New Mexico Land of Enchantment Award for Young Adult (2011)', 'Eliot Rosewater Indiana High School Book Award (2010)', 'The Inky Awards for Silver Inky (2009)', 'California Young Readers Medal for Young Adult (2011)', 'Lincoln Award (2011)', 'Kinderboekwinkelprijs (2010)', 'Missouri Truman Readers Award (2011)', 'CYBILS Award for Young Adult Fantasy & Science Fiction (2008)', 'Literaturpreis der Jury der jungen Leser for Jugendbuch (2010)', 'The Inky Awards Shortlist for Silver Inky (2009)', 'Prix Et-lisez-moi (2011)', 'Missouri Gateway Readers Award (2011)', 'Oklahoma Sequoyah Award for High School and Intermediate (2011)', 'Premio El Templo de las Mil Puertas for Mejor novela extranjera perteneciente a saga (2009)', \"Rebecca Caudill Young Readers' Book Award (2011)\", 'LovelyBooks Leserpreis for Fantasy (2009)', 'LovelyBooks Leserpreis for Bestes Cover/Umschlag (2009)', 'Premi Protagonista Jove for Categoria 13-14 anys (2010)']",
         "Genres": "['Young Adult', 'Fiction', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/1934.Little_Women",
         "N pag": 374,
         "Rating Count": 6684550,
         "Rating Value": 4.32,
         "Review Count": 175488,
         "Title": "The Hunger Games",
         "Unnamed: 0": 21,
         "_deepnote_index_column": 21,
         "award_number": 41,
         "mean_norm_ratings": 24.17424242424248,
         "min_max": 77.50000000000001,
         "series": 1
        },
        {
         "1st Pub": "1937.0",
         "Author": "J.R.R. Tolkien",
         "Awards": "['Keith Barker Millennium Book Award', 'Books I Loved Best Yearly (BILBY) Awards for Older Readers (1997)', 'Mythopoeic Scholarship Award for Inklings Studies (1990)']",
         "Genres": "['Fantasy', 'Classics', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/5907.The_Hobbit_or_There_and_Back_Again",
         "N pag": 366,
         "Rating Count": 3044062,
         "Rating Value": 4.28,
         "Review Count": 51220,
         "Title": "The Hobbit, or There and Back Again",
         "Unnamed: 0": 22,
         "_deepnote_index_column": 22,
         "award_number": 3,
         "mean_norm_ratings": 21.174242424242472,
         "min_max": 74.50000000000001,
         "series": 1
        },
        {
         "1st Pub": "1937.0",
         "Author": "John Steinbeck",
         "Awards": "[\"New York Drama Critics' Circle Award for Best American Play (1938)\"]",
         "Genres": "['Classics', 'Fiction', 'Academic']",
         "Link": "https://www.goodreads.com/book/show/890.Of_Mice_and_Men",
         "N pag": 103,
         "Rating Count": 2028241,
         "Rating Value": 3.88,
         "Review Count": 36305,
         "Title": "Of Mice and Men",
         "Unnamed: 0": 23,
         "_deepnote_index_column": 23,
         "award_number": 1,
         "mean_norm_ratings": -8.82575757575755,
         "min_max": 44.49999999999999,
         "series": 0
        },
        {
         "1st Pub": "1960.0",
         "Author": "Dr. Seuss",
         "Awards": "[]",
         "Genres": "['Childrens', 'Childrens', 'Picture Books']",
         "Link": "https://www.goodreads.com/book/show/23772.Green_Eggs_and_Ham",
         "N pag": 64,
         "Rating Count": 651786,
         "Rating Value": 4.29,
         "Review Count": 9779,
         "Title": "Green Eggs and Ham",
         "Unnamed: 0": 24,
         "_deepnote_index_column": 24,
         "award_number": 1,
         "mean_norm_ratings": 21.924242424242458,
         "min_max": 75.25,
         "series": 0
        },
        {
         "1st Pub": "1999.0",
         "Author": "J.K. Rowling",
         "Awards": "['Bram Stoker Award for Best Work for Young Readers (1999)', 'Hugo Award Nominee for Best Novel (2000)', 'Locus Award for Best Fantasy Novel (2000)', \"Whitbread Award for Children's Book of the Year (1999)\", \"Mythopoeic Fantasy Award for Children's Literature (2008)\", 'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2005)', 'Colorado Blue Spruce Young Adult Book Award (2004)', 'Maine Student Book Award (2001)', 'Golden Archer Award for Intermediate (2001)', 'Indian Paintbrush Book Award (2004)', 'Soaring Eagle Book Award (2002)', 'Hotze de Roosprijs (2001)', 'Nestlé Smarties Book Prize for 9–11 years (1999)']",
         "Genres": "['Fantasy', 'Young Adult', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/13079982-fahrenheit-451",
         "N pag": 435,
         "Rating Count": 3003995,
         "Rating Value": 4.57,
         "Review Count": 59251,
         "Title": "Harry Potter and the Prisoner of Azkaban",
         "Unnamed: 0": 25,
         "_deepnote_index_column": 25,
         "award_number": 13,
         "mean_norm_ratings": 42.92424242424247,
         "min_max": 96.25000000000001,
         "series": 1
        },
        {
         "1st Pub": "1953.0",
         "Author": "Ray Bradbury",
         "Awards": "['Prometheus Hall of Fame Award (1984)', 'Geffen Award for Best Translated SF Book (2002)', 'California Book Award for Fiction (Silver) (1953)', 'Retro Hugo Award for Best Novel (2004)']",
         "Genres": "['Classics', 'Fiction', 'Science Fiction']",
         "Link": "https://www.goodreads.com/book/show/5.Harry_Potter_and_the_Prisoner_of_Azkaban",
         "N pag": 194,
         "Rating Count": 1784898,
         "Rating Value": 3.99,
         "Review Count": 51196,
         "Title": "Fahrenheit 451",
         "Unnamed: 0": 26,
         "_deepnote_index_column": 26,
         "award_number": 4,
         "mean_norm_ratings": -0.5757575757575264,
         "min_max": 52.750000000000014,
         "series": 0
        },
        {
         "1st Pub": "1871.0",
         "Author": "Lewis Carroll",
         "Awards": "[]",
         "Genres": "['Classics', 'Fantasy', 'Fiction']",
         "Link": "https://www.goodreads.com/book/show/24213.Alice_s_Adventures_in_Wonderland_Through_the_Looking_Glass",
         "N pag": 239,
         "Rating Count": 479233,
         "Rating Value": 4.06,
         "Review Count": 11209,
         "Title": "Alice's Adventures in Wonderland / Through the Looking-Glass",
         "Unnamed: 0": 27,
         "_deepnote_index_column": 27,
         "award_number": 1,
         "mean_norm_ratings": 4.674242424242428,
         "min_max": 57.99999999999997,
         "series": 1
        },
        {
         "1st Pub": "1847.0",
         "Author": "Emily Brontë",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Romance']",
         "Link": "https://www.goodreads.com/book/show/6185.Wuthering_Heights",
         "N pag": 464,
         "Rating Count": 1408755,
         "Rating Value": 3.87,
         "Review Count": 40202,
         "Title": "Wuthering Heights",
         "Unnamed: 0": 28,
         "_deepnote_index_column": 28,
         "award_number": 1,
         "mean_norm_ratings": -9.575757575757535,
         "min_max": 43.75000000000001,
         "series": 0
        },
        {
         "1st Pub": "1936.0",
         "Author": "Margaret Mitchell",
         "Awards": "['Pulitzer Prize for Novel (1937)', 'National Book Award for Novel (1936)']",
         "Genres": "['Classics', 'Historical', 'Historical Fiction']",
         "Link": "https://www.goodreads.com/book/show/18405.Gone_with_the_Wind",
         "N pag": 1037,
         "Rating Count": 1102546,
         "Rating Value": 4.3,
         "Review Count": 20495,
         "Title": "Gone with the Wind",
         "Unnamed: 0": 29,
         "_deepnote_index_column": 29,
         "award_number": 2,
         "mean_norm_ratings": 22.674242424242443,
         "min_max": 75.99999999999999,
         "series": 0
        },
        {
         "1st Pub": "1956.0",
         "Author": "Elie Wiesel",
         "Awards": "[]",
         "Genres": "['Nonfiction', 'Classics', 'History']",
         "Link": "https://www.goodreads.com/book/show/1617.Night",
         "N pag": 115,
         "Rating Count": 1015232,
         "Rating Value": 4.34,
         "Review Count": 30286,
         "Title": "Night",
         "Unnamed: 0": 30,
         "_deepnote_index_column": 30,
         "award_number": 1,
         "mean_norm_ratings": 25.674242424242443,
         "min_max": 78.99999999999999,
         "series": 1
        },
        {
         "1st Pub": "1890.0",
         "Author": "Oscar Wilde",
         "Awards": "[]",
         "Genres": "['Classics', 'Fiction', 'Horror']",
         "Link": "https://www.goodreads.com/book/show/5297.The_Picture_of_Dorian_Gray",
         "N pag": 272,
         "Rating Count": 1033391,
         "Rating Value": 4.09,
         "Review Count": 34160,
         "Title": "The Picture of Dorian Gray",
         "Unnamed: 0": 31,
         "_deepnote_index_column": 31,
         "award_number": 1,
         "mean_norm_ratings": 6.924242424242447,
         "min_max": 60.24999999999999,
         "series": 0
        },
        {
         "1st Pub": "1611.0",
         "Author": "Anonymous",
         "Awards": "[]",
         "Genres": "['Religion', 'Classics', 'Nonfiction']",
         "Link": "https://www.goodreads.com/book/show/1923820.Holy_Bible",
         "N pag": 1590,
         "Rating Count": 229592,
         "Rating Value": 4.41,
         "Review Count": 5769,
         "Title": "Holy Bible: King James Version",
         "Unnamed: 0": 32,
         "_deepnote_index_column": 32,
         "award_number": 1,
         "mean_norm_ratings": 30.924242424242465,
         "min_max": 84.25,
         "series": 0
        }
       ]
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Link</th>\n",
       "      <th>Title</th>\n",
       "      <th>Author</th>\n",
       "      <th>Review Count</th>\n",
       "      <th>Rating Count</th>\n",
       "      <th>Rating Value</th>\n",
       "      <th>1st Pub</th>\n",
       "      <th>series</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Awards</th>\n",
       "      <th>N pag</th>\n",
       "      <th>award_number</th>\n",
       "      <th>mean_norm_ratings</th>\n",
       "      <th>min_max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>https://www.goodreads.com/book/show/2657.To_Ki...</td>\n",
       "      <td>To Kill a Mockingbird</td>\n",
       "      <td>Harper Lee</td>\n",
       "      <td>95090</td>\n",
       "      <td>4747905</td>\n",
       "      <td>4.28</td>\n",
       "      <td>1960.0</td>\n",
       "      <td>1</td>\n",
       "      <td>['Classics', 'Fiction', 'Historical']</td>\n",
       "      <td>['Pulitzer Prize for Fiction (1961)', 'Audie A...</td>\n",
       "      <td>324</td>\n",
       "      <td>4</td>\n",
       "      <td>21.174242</td>\n",
       "      <td>74.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>https://www.goodreads.com/book/show/3.Harry_Po...</td>\n",
       "      <td>Harry Potter and the Sorcerer's Stone</td>\n",
       "      <td>J.K. Rowling</td>\n",
       "      <td>118948</td>\n",
       "      <td>7504080</td>\n",
       "      <td>4.48</td>\n",
       "      <td>1997.0</td>\n",
       "      <td>1</td>\n",
       "      <td>['Fantasy', 'Fiction', 'Young Adult']</td>\n",
       "      <td>[\"Mythopoeic Fantasy Award for Children's Lite...</td>\n",
       "      <td>309</td>\n",
       "      <td>28</td>\n",
       "      <td>36.174242</td>\n",
       "      <td>89.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>https://www.goodreads.com/book/show/1885.Pride...</td>\n",
       "      <td>The Diary of a Young Girl</td>\n",
       "      <td>Anne Frank</td>\n",
       "      <td>30804</td>\n",
       "      <td>2912898</td>\n",
       "      <td>4.16</td>\n",
       "      <td>1947.0</td>\n",
       "      <td>0</td>\n",
       "      <td>['Nonfiction', 'Classics', 'History']</td>\n",
       "      <td>['Luisterboek Award Nominee (2008)']</td>\n",
       "      <td>283</td>\n",
       "      <td>1</td>\n",
       "      <td>12.174242</td>\n",
       "      <td>65.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>https://www.goodreads.com/book/show/48855.The_...</td>\n",
       "      <td>Pride and Prejudice</td>\n",
       "      <td>Jane Austen</td>\n",
       "      <td>73295</td>\n",
       "      <td>3185479</td>\n",
       "      <td>4.27</td>\n",
       "      <td>1813.0</td>\n",
       "      <td>0</td>\n",
       "      <td>['Classics', 'Fiction', 'Romance']</td>\n",
       "      <td>[]</td>\n",
       "      <td>279</td>\n",
       "      <td>1</td>\n",
       "      <td>20.424242</td>\n",
       "      <td>73.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>https://www.goodreads.com/book/show/170448.Ani...</td>\n",
       "      <td>The Little Prince</td>\n",
       "      <td>Antoine de Saint-Exupéry</td>\n",
       "      <td>43183</td>\n",
       "      <td>1481259</td>\n",
       "      <td>4.31</td>\n",
       "      <td>1943.0</td>\n",
       "      <td>0</td>\n",
       "      <td>['Classics', 'Fiction', 'Fantasy']</td>\n",
       "      <td>['Retro Hugo Award for Best Novella (2019)']</td>\n",
       "      <td>93</td>\n",
       "      <td>1</td>\n",
       "      <td>23.424242</td>\n",
       "      <td>76.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>94</th>\n",
       "      <td>94</td>\n",
       "      <td>https://www.goodreads.com/book/show/662.Atlas_...</td>\n",
       "      <td>القرآن الكريم</td>\n",
       "      <td>Anonymous</td>\n",
       "      <td>3146</td>\n",
       "      <td>59042</td>\n",
       "      <td>4.35</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>['Religion', 'Religion', 'Islam']</td>\n",
       "      <td>[]</td>\n",
       "      <td>604</td>\n",
       "      <td>1</td>\n",
       "      <td>26.424242</td>\n",
       "      <td>79.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>95</td>\n",
       "      <td>https://www.goodreads.com/book/show/4934.The_B...</td>\n",
       "      <td>The Book of Mormon: Another Testament of Jesus...</td>\n",
       "      <td>Anonymous</td>\n",
       "      <td>6021</td>\n",
       "      <td>77516</td>\n",
       "      <td>4.32</td>\n",
       "      <td>1830.0</td>\n",
       "      <td>0</td>\n",
       "      <td>['Religion', 'Nonfiction', 'Christianity']</td>\n",
       "      <td>[]</td>\n",
       "      <td>531</td>\n",
       "      <td>1</td>\n",
       "      <td>24.174242</td>\n",
       "      <td>77.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>96</td>\n",
       "      <td>https://www.goodreads.com/book/show/323355.The...</td>\n",
       "      <td>The Brothers Karamazov</td>\n",
       "      <td>Fyodor Dostoyevsky</td>\n",
       "      <td>11994</td>\n",
       "      <td>255569</td>\n",
       "      <td>4.32</td>\n",
       "      <td>1879.0</td>\n",
       "      <td>1</td>\n",
       "      <td>['Classics', 'Fiction', 'Cultural']</td>\n",
       "      <td>[]</td>\n",
       "      <td>796</td>\n",
       "      <td>1</td>\n",
       "      <td>24.174242</td>\n",
       "      <td>77.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>97</td>\n",
       "      <td>https://www.goodreads.com/book/show/7244.The_P...</td>\n",
       "      <td>The Poisonwood Bible</td>\n",
       "      <td>Barbara Kingsolver</td>\n",
       "      <td>23753</td>\n",
       "      <td>672550</td>\n",
       "      <td>4.07</td>\n",
       "      <td>1998.0</td>\n",
       "      <td>0</td>\n",
       "      <td>['Fiction', 'Historical', 'Historical Fiction']</td>\n",
       "      <td>['Pulitzer Prize Nominee for Fiction (1999)', ...</td>\n",
       "      <td>546</td>\n",
       "      <td>8</td>\n",
       "      <td>5.424242</td>\n",
       "      <td>58.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>98</td>\n",
       "      <td>https://www.goodreads.com/book/show/153747.Mob...</td>\n",
       "      <td>Moby-Dick or, the Whale</td>\n",
       "      <td>Herman Melville</td>\n",
       "      <td>16621</td>\n",
       "      <td>491913</td>\n",
       "      <td>3.51</td>\n",
       "      <td>1851.0</td>\n",
       "      <td>0</td>\n",
       "      <td>['Classics', 'Fiction', 'Literature']</td>\n",
       "      <td>['Audie Award for Solo Narration - Male (2006)...</td>\n",
       "      <td>654</td>\n",
       "      <td>2</td>\n",
       "      <td>-36.575758</td>\n",
       "      <td>16.75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>99 rows × 15 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Unnamed: 0                                               Link  \\\n",
       "0            0  https://www.goodreads.com/book/show/2657.To_Ki...   \n",
       "1            1  https://www.goodreads.com/book/show/3.Harry_Po...   \n",
       "2            2  https://www.goodreads.com/book/show/1885.Pride...   \n",
       "3            3  https://www.goodreads.com/book/show/48855.The_...   \n",
       "4            4  https://www.goodreads.com/book/show/170448.Ani...   \n",
       "..         ...                                                ...   \n",
       "94          94  https://www.goodreads.com/book/show/662.Atlas_...   \n",
       "95          95  https://www.goodreads.com/book/show/4934.The_B...   \n",
       "96          96  https://www.goodreads.com/book/show/323355.The...   \n",
       "97          97  https://www.goodreads.com/book/show/7244.The_P...   \n",
       "98          98  https://www.goodreads.com/book/show/153747.Mob...   \n",
       "\n",
       "                                                Title  \\\n",
       "0                               To Kill a Mockingbird   \n",
       "1               Harry Potter and the Sorcerer's Stone   \n",
       "2                           The Diary of a Young Girl   \n",
       "3                                 Pride and Prejudice   \n",
       "4                                   The Little Prince   \n",
       "..                                                ...   \n",
       "94                                      القرآن الكريم   \n",
       "95  The Book of Mormon: Another Testament of Jesus...   \n",
       "96                             The Brothers Karamazov   \n",
       "97                               The Poisonwood Bible   \n",
       "98                            Moby-Dick or, the Whale   \n",
       "\n",
       "                      Author  Review Count  Rating Count  Rating Value  \\\n",
       "0                 Harper Lee         95090       4747905          4.28   \n",
       "1               J.K. Rowling        118948       7504080          4.48   \n",
       "2                 Anne Frank         30804       2912898          4.16   \n",
       "3                Jane Austen         73295       3185479          4.27   \n",
       "4   Antoine de Saint-Exupéry         43183       1481259          4.31   \n",
       "..                       ...           ...           ...           ...   \n",
       "94                 Anonymous          3146         59042          4.35   \n",
       "95                 Anonymous          6021         77516          4.32   \n",
       "96        Fyodor Dostoyevsky         11994        255569          4.32   \n",
       "97        Barbara Kingsolver         23753        672550          4.07   \n",
       "98           Herman Melville         16621        491913          3.51   \n",
       "\n",
       "    1st Pub  series                                           Genres  \\\n",
       "0    1960.0       1            ['Classics', 'Fiction', 'Historical']   \n",
       "1    1997.0       1            ['Fantasy', 'Fiction', 'Young Adult']   \n",
       "2    1947.0       0            ['Nonfiction', 'Classics', 'History']   \n",
       "3    1813.0       0               ['Classics', 'Fiction', 'Romance']   \n",
       "4    1943.0       0               ['Classics', 'Fiction', 'Fantasy']   \n",
       "..      ...     ...                                              ...   \n",
       "94      NaN       0                ['Religion', 'Religion', 'Islam']   \n",
       "95   1830.0       0       ['Religion', 'Nonfiction', 'Christianity']   \n",
       "96   1879.0       1              ['Classics', 'Fiction', 'Cultural']   \n",
       "97   1998.0       0  ['Fiction', 'Historical', 'Historical Fiction']   \n",
       "98   1851.0       0            ['Classics', 'Fiction', 'Literature']   \n",
       "\n",
       "                                               Awards  N pag  award_number  \\\n",
       "0   ['Pulitzer Prize for Fiction (1961)', 'Audie A...    324             4   \n",
       "1   [\"Mythopoeic Fantasy Award for Children's Lite...    309            28   \n",
       "2                ['Luisterboek Award Nominee (2008)']    283             1   \n",
       "3                                                  []    279             1   \n",
       "4        ['Retro Hugo Award for Best Novella (2019)']     93             1   \n",
       "..                                                ...    ...           ...   \n",
       "94                                                 []    604             1   \n",
       "95                                                 []    531             1   \n",
       "96                                                 []    796             1   \n",
       "97  ['Pulitzer Prize Nominee for Fiction (1999)', ...    546             8   \n",
       "98  ['Audie Award for Solo Narration - Male (2006)...    654             2   \n",
       "\n",
       "    mean_norm_ratings  min_max  \n",
       "0           21.174242    74.50  \n",
       "1           36.174242    89.50  \n",
       "2           12.174242    65.50  \n",
       "3           20.424242    73.75  \n",
       "4           23.424242    76.75  \n",
       "..                ...      ...  \n",
       "94          26.424242    79.75  \n",
       "95          24.174242    77.50  \n",
       "96          24.174242    77.50  \n",
       "97           5.424242    58.75  \n",
       "98         -36.575758    16.75  \n",
       "\n",
       "[99 rows x 15 columns]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('Books.csv')\n",
    "cols = ['Unnamed: 0','Link','Title','Author','Review Count','Rating Count','Rating Value','1st Pub','series','Genres','Awards','N pag']\n",
    "data[\"1st Pub\"].dropna().astype(\"int\")\n",
    "df = data[cols]\n",
    "df\n",
    "\n",
    "\n",
    "#number of awards\n",
    "awards_number = [len(awards.split(',')) for awards in df['Awards']]\n",
    "df[\"award_number\"]= awards_number\n",
    "\n",
    "    #normalizations\n",
    "maxr=df[\"Rating Value\"].max()\n",
    "minr =df[\"Rating Value\"].min()\n",
    "meanr= df[\"Rating Value\"].mean()\n",
    "#mean_normalization\n",
    "df['mean_norm_ratings'] = 10 + ((df['Rating Value']- meanr) / (maxr- minr))*90\n",
    "\n",
    "#min-max normalization\n",
    "df['min_max'] = 10 + ((df['Rating Value']-minr)/(maxr-minr))*90\n",
    "\n",
    "df\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00001-f24f2997-c622-4533-b05b-ab47d5c74523",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "## EDA"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00006-c271ae13-26f4-4f19-9448-1544f34c5bc8",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "### Checking the Correlation between number of pages of the book and the average ratings of it.\n",
    "#### Exploring whether the average ratings given has anything to do with the thickness of the book"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "cell_id": "00003-c5ecdcb9-914a-4411-83e5-fb3b7deef532",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": true,
    "execution_millis": 173,
    "execution_start": 1618346174609,
    "source_hash": "cbebc28b",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#1 Create a 2D scatterplot with pages on the x-axis and num_ratings on the y-axis. \n",
    "\n",
    "plt.figure(figsize=(8,8))\n",
    "#colors = cm.viridis(np.random.randint(100))\n",
    "plt.scatter(df[\"N pag\"].values,df[\"Rating Value\"] , color='#3498db') \n",
    "plt.title('Scatter plot ')\n",
    "plt.xlabel('Number of pages')\n",
    "plt.ylabel('Average Ratings');\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00008-21d8cf6f-8750-47d1-aba6-d8e9af844092",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "#### We can deduce from the very helpfull graph that from the Top 100 books in the sample that the number of pages does indeed affect the average ratings. Firstlly we can note that there are more books that have fewer than 1000 pages in the Top100 and that the min rating is 3.4. However as we gather more data, we would be able to tell a more concrete story."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00009-87e35264-9f88-497e-b387-a34d08153b6f",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "### Checking the Correlation between number of pages of the book and the number of ratings.\n",
    "#### Exploring  whether the number of ratings given has anything to do with the thickness of the book"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "cell_id": "00009-1495b59b-c70f-400a-9566-735c78741364",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 172,
    "execution_start": 1618327958297,
    "source_hash": "b9f0ab60",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "plt.figure(figsize=(8,8))\n",
    "#colors = cm.viridis(np.random.randint(100))\n",
    "plt.scatter(df[\"N pag\"].values,df[\"Rating Count\"] , color='#3498db') \n",
    "plt.title('Scatter plot ')\n",
    "plt.xlabel('Number of pages')\n",
    "plt.ylabel('Number of Ratings');\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "cell_id": "00010-420a66d5-f271-47b1-9ef8-f8b574ba3372",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 154,
    "execution_start": 1618325271909,
    "source_hash": "edf86ad4",
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "covariance[[1.56104137e+05 1.68887920e+01]\n",
      " [1.68887920e+01 5.59050917e-02]]\n",
      "correlation(0.18078637582550142, 0.07333454101759868)\n"
     ]
    }
   ],
   "source": [
    "#Can you compute numerically the correlation coefficient of these two columns?\n",
    "#Visualise the avg_rating distribution.\n",
    "covariance = np.cov(df[\"N pag\"],df[\"Rating Value\"] )\n",
    "correlation = pearsonr(df[\"N pag\"],df[\"Rating Value\"] )\n",
    "print(\"covariance\" + str(covariance))\n",
    "print(\"correlation\" + str(correlation))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "cell_id": "00011-daa91892-21e9-45b6-953d-a09827228aee",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 448,
    "execution_start": 1618323958556,
    "source_hash": "64ce8953",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 504x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "corr = df.corr()\n",
    "\n",
    "mask = np.triu(np.ones_like(corr, dtype=bool))\n",
    "cmap = sns.diverging_palette(230, 20, as_cmap=True)\n",
    "sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,\n",
    "            square=True, linewidths=.5, cbar_kws={\"shrink\": .5})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00011-6de28265-abd9-47d9-a756-40c9e6585e2d",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "#### We checked if there is any other features that could help us understand why people have really gone out of there way to recommend these books and potentially why some books have a lower rating and awards. There is a strong correlation between awards and the number of reviews and ratings. This shows that the boook community do have a big say in which book actually grabs a lot of awards."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00012-67e3b35e-aaaf-4a88-a334-98c3077fc636",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "#### Furthermoreit can be seen that the number of pages and number of reviews&ratings are negatively correlated. It is interesting and shall be monitored further. Even though the magnitude is almost negligble.\n",
    "#### We often complain how movies sequels dont do too well, with books that does not seem to be the case,the average rating seems to be highly correlated to whether the book has sequel.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "cell_id": "00004-69edb838-9f3f-4294-906f-5c7cabf9e590",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 298,
    "execution_start": 1618325603342,
    "source_hash": "9f17087f",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x7fd88e6566d0>"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#3Visualise the avg_rating distribution.\n",
    "sns.displot(df['Rating Value'], bins= 20, edgecolor= \"white\", kde= True, alpha= 0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "cell_id": "00014-b978eaa8-2359-4c98-aeec-810712e3130f",
    "deepnote_cell_type": "code",
    "tags": []
   },
   "outputs": [],
   "source": [
    "## The distribution of the ratings is quite negatively skewed and the mean is around 4.3, which would be something \n",
    "##of no surprise to us as this are the creme de la creme of books."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "cell_id": "00004-4d9d4283-6f52-49a0-8173-59dd22e376b5",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 286,
    "execution_start": 1618311649000,
    "source_hash": "c00083bd",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 6.79999999999999, 'mean_norm_rating distribution')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#5Visualise the mean_norm_rating distribution.  fit=norm\n",
    "\n",
    "\n",
    "sns.displot(df['mean_norm_ratings'], bins= 20, edgecolor= \"white\",kde= True, alpha= 0.65, color= '#008367')\n",
    "plt.xlabel(\"mean_norm_rating distribution\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "cell_id": "00013-15b73a22-c366-4f03-bfd7-990128125b40",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 1,
    "execution_start": 1618315717274,
    "source_hash": "e84c4363",
    "tags": []
   },
   "outputs": [],
   "source": [
    "#7 What is the best fit in terms of a distribution (normal, chi-squared...) to represent each of those graphs? \n",
    "\n",
    "mpl.style.use(\"ggplot\")\n",
    "\n",
    "def danoes_formula(data):\n",
    "    \n",
    "    N = len(data)\n",
    "    skewness = st.skew(data)\n",
    "    sigma_g1 = math.sqrt((6*(N-2))/((N+1)*(N+3)))\n",
    "    num_bins = 1 + math.log(N,2) + math.log(1+abs(skewness)/sigma_g1,2)\n",
    "    num_bins = round(num_bins)\n",
    "    return num_bins\n",
    "\n",
    "def plot_histogram(data, results, n):\n",
    "    ## n first distribution of the ranking\n",
    "    N_DISTRIBUTIONS = {k: results[k] for k in list(results)[:n]}\n",
    "\n",
    "    ## Histogram of data\n",
    "    plt.figure(figsize=(10, 5))\n",
    "    plt.hist(data, density=True, ec='white', color=(63/235, 149/235, 170/235))\n",
    "    plt.title('HISTOGRAM')\n",
    "    plt.xlabel('Values')\n",
    "    plt.ylabel('Frequencies')\n",
    "\n",
    "    ## Plot n distributions\n",
    "    for distribution, result in N_DISTRIBUTIONS.items():\n",
    "        # print(i, distribution)\n",
    "        sse = result[0]\n",
    "        arg = result[1]\n",
    "        loc = result[2]\n",
    "        scale = result[3]\n",
    "        x_plot = np.linspace(min(data), max(data), 1000)\n",
    "        y_plot = distribution.pdf(x_plot, loc=loc, scale=scale, *arg)\n",
    "        plt.plot(x_plot, y_plot, label=str(distribution)[32:-34] + \": \" + str(sse)[0:6], color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))\n",
    "    \n",
    "    plt.legend(title='DISTRIBUTIONS', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "    plt.show()\n",
    "\n",
    "def fit_data(data):\n",
    "    ## st.frechet_r,st.frechet_l: are disbled in current SciPy version\n",
    "    ## st.levy_stable: a lot of time of estimation parameters\n",
    "    ALL_DISTRIBUTIONS = [        \n",
    "        st.alpha,st.anglit,st.arcsine,st.beta,st.betaprime,st.bradford,st.burr,st.cauchy,st.chi,st.chi2,st.cosine,\n",
    "        st.dgamma,st.dweibull,st.erlang,st.expon,st.exponnorm,st.exponweib,st.exponpow,st.f,st.fatiguelife,st.fisk,\n",
    "        st.foldcauchy,st.foldnorm, st.genlogistic,st.genpareto,st.gennorm,st.genexpon,\n",
    "        st.genextreme,st.gausshyper,st.gamma,st.gengamma,st.genhalflogistic,st.gilbrat,st.gompertz,st.gumbel_r,\n",
    "        st.gumbel_l,st.halfcauchy,st.halflogistic,st.halfnorm,st.halfgennorm,st.hypsecant,st.invgamma,st.invgauss,\n",
    "        st.invweibull,st.johnsonsb,st.johnsonsu,st.ksone,st.kstwobign,st.laplace,st.levy,st.levy_l,\n",
    "        st.logistic,st.loggamma,st.loglaplace,st.lognorm,st.lomax,st.maxwell,st.mielke,st.nakagami,st.ncx2,st.ncf,\n",
    "        st.nct,st.norm,st.pareto,st.pearson3,st.powerlaw,st.powerlognorm,st.powernorm,st.rdist,st.reciprocal,\n",
    "        st.rayleigh,st.rice,st.recipinvgauss,st.semicircular,st.t,st.triang,st.truncexpon,st.truncnorm,st.tukeylambda,\n",
    "        st.uniform,st.vonmises,st.vonmises_line,st.wald,st.weibull_min,st.weibull_max,st.wrapcauchy\n",
    "    ]\n",
    "    \n",
    "    MY_DISTRIBUTIONS = [st.beta, st.expon, st.norm, st.uniform, st.johnsonsb, st.gennorm, st.gausshyper]\n",
    "\n",
    "    ## Calculae Histogram\n",
    "    num_bins = danoes_formula(data)\n",
    "    frequencies, bin_edges = np.histogram(data, num_bins, density=True)\n",
    "    central_values = [(bin_edges[i] + bin_edges[i+1])/2 for i in range(len(bin_edges)-1)]\n",
    "\n",
    "    results = {}\n",
    "    for distribution in MY_DISTRIBUTIONS:\n",
    "        ## Get parameters of distribution\n",
    "        params = distribution.fit(data)\n",
    "        \n",
    "        ## Separate parts of parameters\n",
    "        arg = params[:-2]\n",
    "        loc = params[-2]\n",
    "        scale = params[-1]\n",
    "    \n",
    "        ## Calculate fitted PDF and error with fit in distribution\n",
    "        pdf_values = [distribution.pdf(c, loc=loc, scale=scale, *arg) for c in central_values]\n",
    "        \n",
    "        ## Calculate SSE (sum of squared estimate of errors)\n",
    "        sse = np.sum(np.power(frequencies - pdf_values, 2.0))\n",
    "        \n",
    "        ## Build results and sort by sse\n",
    "        results[distribution] = [sse, arg, loc, scale]\n",
    "        \n",
    "    results = {k: results[k] for k in sorted(results, key=results.get)}\n",
    "    return results\n",
    "        \n",
    "def main():\n",
    "    ## Import data\n",
    "    data = pd.Series(sm.datasets.elnino.load_pandas().data.set_index('YEAR').values.ravel())\n",
    "    results = fit_data(data)\n",
    "    plot_histogram(data, results, 5)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "cell_id": "00006-e337319c-0651-4f07-ad5b-f4b8abaf9817",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 284,
    "execution_start": 1618311920382,
    "source_hash": "5de23a1",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x7fd86df0f350>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#4min max rating distribution\n",
    "plt.rcParams.update({'figure.figsize':(7,5)})\n",
    "#plt.hist(df.min_max, bins= 20) #we could change the bins\n",
    "sns.displot(df['min_max'], bins= 20, edgecolor= \"white\", kde= True, alpha= 0.75)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "cell_id": "00006-a52542c7-66cf-46de-bd3e-ff98a3538155",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 199,
    "execution_start": 1618312029819,
    "source_hash": "bed28e3d",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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u+xJfWvmn26NcfjwYV133XUaO3asRo8ereXLl0uStm3bpksvvVRjxozRmDFj9Lvf/U6S9PLLL2v8+PGqqKjQiBEjdNVVV51yxHVJmjt3rhYsWPC5+XV1dbr22ms1cuRIjR49WmvWrJGUukfVtGnTNGHCBE2cOFGLFi3SjBkzNGnSJJWWluqBBx7Qvffeq9GjR+viiy/W3r17O/waEVAA0AVmXPlN/dfTT6murk5b3q7Sn40d27RswYIFmjBhgt58802tWbNGc+fO1eHDh3XmmWdq1apVWr9+vX71q1/p+9//ftNzNmzYoPvvv1/V1dX66KOP9Nvf/vaU2x83bpx69OjRFECfefDBB2Vm2rx5s5YsWaLZs2c3jXq+fv16LVu2TK+88ookqaqqSs8884zWrl2refPmqaioSBs2bNC4ceP02GOPdfg1IqAAoAuUfWmkPtm+Xc8ue1ITJ00+btlLL72kO++8U6NGjdL48eNVV1en7du3q6GhQddff71Gjhypb37zm6qurm56ztixY1VSUqKCggKNGjVK27Zta7WG+fPn64477jhu3muvvaarr75akjRixAidc845eu+99yRJkyZN0sCBf7pFzFe/+lX17dtXxcXF6t+/v77xjW9ISt16Pp3tt4ZzUADQRSZP/Qv90/wff+5+UO6up59+WsOHDz9u/dtuu02DBg3SW2+9pWQyqV69ejUta37PqG7duimRaH0A3AkTJmj+/Pl6/fXX06q3d+/ex00332ZBQUHTdEFBQVrbbw3voACgi7R0P6jJkyfrZz/7WdN5pA0bNkiS9u/fr8GDB6ugoECPP/64Ghtbv3Nva+bPn6+77767afrSSy/VE088IUl67733tH379s8FZWfhHRSA/Nazb+rWJ+lyV7dWLjNPV0v3g/rpT3+qm2++WRdccIGSyaSGDRumlStX6sYbb9SVV16pxx57TFOmTPncO5r2mDp1qoqLi5umb7zxRt1www0aOXKkCgsLtWjRouPeKXUm7gcFtIb7QeWUk92PqC0ydbsN7gf1+ftB0cUHAAgSXXwAkKOuuOIKbd269bh5d911lyZPntzCM8JCQAFAjnr22We7uoQOoYsPQN7pzHPv+JO2vu4EFIC80qtXL+3Zs4eQ6mTurj179hz32a3W0MUHIK+UlJSopqZGu3fvbtfzE8mkjtR3/PNHJ9rVs5sK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\n",
      "text/plain": [
       "<Figure size 504x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#### min-max & mean-norm\n",
    "plt.rcParams.update({'figure.figsize':(7,5)})\n",
    "plt.hist(df['min_max'], alpha=0.5, label='Min-Max', edgecolor= \"w\")\n",
    "plt.hist(df['mean_norm_ratings'], alpha=0.5, label='Mean_Norm', edgecolor= \"w\")\n",
    "plt.legend(loc='upper right')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00015-d24a099e-6c8f-4fb5-b8fc-4e9178a8abe0",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "## Awards baby"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "cell_id": "00004-7fce8fb5-4e38-4e45-8644-a734e793a738",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 132,
    "execution_start": 1618311649875,
    "source_hash": "3e3ef3fc",
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/shared-libs/python3.7/py/lib/python3.7/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  FutureWarning\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='award_number'>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 504x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure(figsize =(7, 5))\n",
    "\n",
    "\n",
    "sns.boxplot(df['award_number'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "cell_id": "00021-6d5f8848-9e88-4b4d-b7c8-fb5c9ef59655",
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "#### The boxplot is quite interesting as 1st to 3rd Quantile is all piled up between 1-5 and the 4th quantile upto 9 there are quite a lot of outliers too. We want to further explore the possible causes and create an interactive graph\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "cell_id": "00021-f7d457d8-3814-4260-b02a-da85ba195a32",
    "deepnote_cell_type": "code",
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "cell_id": "00019-1d308f05-bb7e-4aa6-a08e-dbd6e6431420",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 151,
    "execution_start": 1618315239690,
    "source_hash": "9b5a1a27",
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'awards')"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 10 Make a scatterplot to represent  minmax_norm_ratings in function of the number of awards won by the book.\n",
    "plt.figure(figsize=(8,8))\n",
    "#colors = cm.viridis(np.random.randint(100))\n",
    "\n",
    "plt.scatter(df[\"min_max\"],df[\"award_number\"] , color='#3498db') \n",
    "plt.title('Scatter plot awards vs ratings')\n",
    "plt.xlabel('min-max norm ratings')\n",
    "plt.ylabel('awards')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "cell_id": "00018-970a0904-850c-4f96-be4b-581d0118a85e",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 1,
    "execution_start": 1618311650001,
    "is_code_hidden": true,
    "source_hash": "d5209e4a",
    "tags": []
   },
   "outputs": [],
   "source": [
    "# 9 Now, make a **simple plot** to visualise the ratings w.r.t. the years!\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "cell_id": "00020-6b9dcfb5-8b58-4564-92ff-2509924f0948",
    "deepnote_cell_type": "code",
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "cell_id": "00006-ab3ccea9-ffe9-49a7-951c-2951fb52eb6f",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": true,
    "execution_millis": 80,
    "is_code_hidden": true,
    "output_cleared": true,
    "source_hash": null,
    "tags": []
   },
   "outputs": [],
   "source": [
    "advert_report = sv.analyze(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "cell_id": "00007-e9e7fa12-ce26-4b6f-abf7-3aaffbf8a66a",
    "deepnote_cell_type": "code",
    "deepnote_to_be_reexecuted": false,
    "execution_millis": 31,
    "execution_start": 1618313953910,
    "is_code_hidden": true,
    "output_cleared": true,
    "source_hash": null,
    "tags": []
   },
   "outputs": [],
   "source": [
    "#analyse\n",
    "\n",
    "#1 Group the books by original_publish_year and get the mean of the minmax_norm_ratings of the groups.\n",
    "df[\"1st Pub\"].dropna()\n",
    "year_means = df.groupby('1st Pub').mean()\n",
    "year_means[0:10]\n",
    "\n",
    "\n",
    "\n",
    "\n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "created_in_deepnote_cell": true,
    "deepnote_cell_type": "markdown",
    "tags": []
   },
   "source": [
    "<a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=b8d5d41e-3ba7-4959-ae1c-b25e3642b110' target=\"_blank\">\n",
    "<img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>\n",
    "Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>"
   ]
  }
 ],
 "metadata": {
  "deepnote": {
   "is_reactive": false
  },
  "deepnote_execution_queue": [
   {
    "cellId": "00003-c5ecdcb9-914a-4411-83e5-fb3b7deef532",
    "msgId": "b8c86042-db1b-472a-8edf-d329cffc006c",
    "sessionId": "b771c4da-4ae7-44c2-9acf-c8c211c51b3d"
   }
  ],
  "deepnote_notebook_id": "a755ac92-5d19-4d47-a87a-898c4019f82d",
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
