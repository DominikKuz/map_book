users: list[dict[str, str]] = [
    {'name': 'Staś', 'surname': 'Grzymski', 'post': 1, 'location':'Konin'},
    {'name': 'Kacper', 'surname': 'Macioch', 'post': 2, 'location':'Ząbki'},
    {'name': 'Michał', 'surname': 'Krzywiński', 'post': 3, 'location':'Brodnica'},
    {'name': 'Tymon', 'surname': 'Leszczyc', 'post': 2, 'location':'Toruń'},
    {'name': 'Michał', 'surname': 'Lębryk', 'post': 2, 'location':'Lublin'},]



def read(users: list[dict[str, str]]) -> None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikował {user["posts"]} postów ')
