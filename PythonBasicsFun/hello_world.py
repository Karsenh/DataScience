# Single line python comment

"""

Multi line python comment

"""


def main():
    print("Hello world!")

# If this module is run directly __name__ == "__main__"
# If this module is imported and ran __name__ == module_name
if __name__ == "__main__":
    print(__name__)
    main()