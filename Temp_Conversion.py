def to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius
def to_fahrenheit(celcius):
    fahrenheit = celcius * 9/5 +32
    return fahrenheit

def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celcius(temp), 2), "Celcius")

    for temp in range(0, 100, 20):
        print(temp, "Celcius =", round(to_fahrenheit(temp), 2), "Fahrenheit")
if __name__ == "__main__":
    main()