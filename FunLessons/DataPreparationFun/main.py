def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []

    for row in table:
        if (row[col_index] != "NA"):
            col.append(row[col_index])

    return col
 


def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
                ["toyota corolla", 75, 2711],
                ["ford pinto", 76, 3025],
                ["toyota corolla", 77, 2789],]

    msrps = get_column(msrp_table, header, "MSRP")
    print(msrps)



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


if __name__ == "__main__":
    main()