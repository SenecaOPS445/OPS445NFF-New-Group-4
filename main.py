# Main function with argparse to handle command line arguments
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser()
    # Define the argument for resource (cpu or ram)
    parser.add_argument('resource', help="Specify 'cpu' for CPU usage or 'ram' for RAM usage.", type=str, default=None)

