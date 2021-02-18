import random
import math
import numpy as np

def get_column(table, header, col_name):

    # Create a var for the index of the col to get by checking its position in the header
    col_index = header.index(col_name)

    # Create an empty array to append the cols from table
    col = []

    # For each row in the passed in table...
    for row in table:
        # If the row has a value (doesn't equal "NA")
        if row[col_index] != "NA":
            # Append the row to the col array
            col.append(row[col_index])

    # Return the col array
    return col

def get_min_max(values):
    # Return multiple values
    # via a tuple (immutable list that is often used to packing and unpacking values)
    return min(values), max(values)

def get_frequencies(table, header, col_name):
    # Isolate a column to check for value / frequencies
    col = get_column(table, header, col_name)

    # Sort the column using python sorth method
    col.sort()
    # Create empty array to store values and frequency counts
    values = []
    counts = []

    # for each value in the col...
    for value in col:
        # if the current value is not in the values array...
        if value not in values:
            # first time we've seen this value - insert it into the values array
            values.append(value)
            counts.append(1)
        else: 
            # we have seen this value before - so the previous count index should be incremented again
            counts[-1] += 1 # OK because list is osrted 

    return values, counts

# 
# Quiz question answers
# 
def generate_rand_table(num_rows, num_cols):
    # Create an empty array to store rows and cols
    randTable = []

    # for each row
    for _ in range(num_rows):
        # create a new row array
        row = []
        # for each col
        for _ in range(num_cols):
            row.append(random.randint(0, 99))
        # Append that row to the table
        randTable.append(row)

    return randTable


def find_min(table):
    mins = []

    for row in table:
        mins.append(min(row))

    return min(mins)


def find_max(table):
    maxes = []
    
    for row in table:
        maxes.append(max(row))

    return max(maxes)
 


def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
                ["toyota corolla", 75, 2711],
                ["ford pinto", 76, 3025],
                ["toyota corolla", 77, 2789],]

    msrps = get_column(msrp_table, header, "MSRP")
    print(msrps)

    # warm up
    modelYear_values, modelYear_counts = get_frequencies(msrp_table, header, "ModelYear")
    print("Model Year Vals: ", modelYear_values, "Model Year Count: ", modelYear_counts)

    # More on attributes
    # 1. what is the type of an attribute?
    # what is the most appropriate way to store the attribute
    # 2. what is the semantic value/type of an attribute
    # what do the values of the attributes mean/represent?
    # domain knowledge!!
    # 3. what is the scale the attribute is recorded on?
    # categorical or continuous
    # nominal: categorical scale without an inherent ordering
    # e.g. names, colors, etc.
    # ordinal: categorical with an odering
    # t-shirt sizes (S, M, L, XL, ...), letter grades (A, A-, B+, ...)
    # Ratio-Scaled: Continous attribute where 0 means "absence"
    # e.g. 0 lbs (absence of weight), 0 degrees K (absence of temperature) 

    # Noisy vs Invalid data
    # Noisy: valid on the sacle, but recorded incorrectly
    # e.g. 18 years old but 81 is entered for age
    # Invalid: not valid on the scale
    # e.g. "bob" is not a valid value on the 'age' scale

    # Missing values
    # Two main ways to deal with missing values
    #  1. (PA1) - Omit / Discard them (not generally the optimal approach)
    #  Only omit when the dataset is large and the number of missing values is small
    #  2. Fill them
    #  Categorical Attribute: Majority voting system (e.g. most frequent val)
    #  Continuous Attribute: central tendency measure (e.g. average, median, etc.)
    #  more on this later: intelligently... (use groups or kNN)

    #  Summary stats
    #  EDA = (Exploratory Data Analysis)
    #  Mid value(mid range):(min + max) / 2
    #  Min, Max - 
    msrp_min, msrp_max = get_min_max(msrps)
    print("min = ", msrp_min, "max = ", msrp_max)
    # artihmetic mean /  central tendency
    msrp_mean = sum(msrps) / len(msrps)
    print("Mean = ", msrp_mean)
    #  Mode: The most frequently occuring value (will do later in histograms)

    # Data dispersion
    #  Variance measures the spread of that data
    #   Low Variance = close to the mean
    #   High Variance = far from the mean
    #  Standard Deviation: Square of teh variance
    #  TODO: Computer variance and std dev and compare with numpy
    #  Talk about quantiles

    # Squared mean deviations is each value - the mean, squared
    squared_mean_deviations = [(x - msrp_mean) ** 2 for x in msrps] # List comprehension

    # Variance is the sum of the squared mean deviations divided by the number of them
    msrp_variance = sum(squared_mean_deviations) / len(squared_mean_deviations)
    print("Varaince = ", msrp_variance)

    # Stdev is the sqrt of the variance
    msrp_stdev = math.sqrt(msrp_variance)
    print("stdev = ", msrp_stdev, np.std(msrps)) # These should be equal





if __name__ == "__main__":
    main()