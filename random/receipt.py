import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[key_column_index]

                dictionary[key] = row_list

    return dictionary

def main():

    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1 

    

    
    products_dict = read_dictionary("products.csv", PRODUCT_INDEX)

    print(products_dict)

    compound_list = []

    with open("request.csv", "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
           
            if len(row_list) != 0:
                product_key = row_list[0]
                if product_key in products_dict:
                 
                 product_details = products_dict[product_key]
                 product_name = product_details[NAME_INDEX]
                 product_price = float(product_details[PRICE_INDEX])  
                 quantity = int(row_list[QUANTITY_INDEX])

                 print(f"{product_name}, {quantity}, {product_price}")
                #here I call the dictionary key value and match it
                #in the list, then print the product name.
                

  




if __name__ == "__main__":
    main()
 
 