from Repository.repository import Repository
from Service.service import Service


def main():
    '''
    Main function
    :return: the output file
    '''
    repository = Repository("Data/input.txt")
    repository.load_file()
    service = Service(repository)
    service.print_tsp(1)
    service.print_shortest_path()


if __name__ == '__main__':
    main()
