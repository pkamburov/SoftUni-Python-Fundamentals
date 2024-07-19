def loading_bar(num: int) -> str:
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent = num // 10
    return f"{num}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
