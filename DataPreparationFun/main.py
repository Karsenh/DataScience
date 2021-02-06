def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []

    for row in table:
        if (row[col_index]) != "NA":
            col.append(row[col_index])

 


def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
                ["toyota corolla", 75, 2711],
                ["ford pinto", 76, 3025],
                ["toyota corolla", 77, 2789],]



    # More on attributes
    # 1. what is the type of an attribute?
    # what is the most appropriate way to store the attribute
    # 2. what is the semantic value/type of an attribute


if __name__ == "__main__":
    main()