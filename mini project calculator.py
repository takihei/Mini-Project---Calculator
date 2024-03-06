import random as rd
def main():
    level = get_level()
    operation=get_operation()
    generate_question(level,operation)
def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level in (1, 2, 3):
                return level
            else:
                raise Exception()
        except (ValueError, Exception):
            pass
def get_operation():
    while True:
        try:
            print("Operations: -Summation -Substraction -Multiplication -Division")
            operation=(input("Operation:")).lower()
            if operation in ("summation","substraction","multiplication"):
                return operation
            elif operation=="division":
                print("Important Note:\nAnswers of the division questions must written in decimal form.\nThey must contain the whole part of the number and the first digit after the decimal point.\nYou must use a dot but a comma to express the decimal point.")
                return operation
            else:
                raise Exception()
        except (ValueError,Exception):
            pass
def generate_question(level,operation):
    if operation=="summation":
        if level == 1:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(0, 9)
                    b = rd.randint(0, 9)
                    c = a + b
                    answer = int(input(f"{a} + {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} + {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} + {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:
                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 2:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(10, 99)
                    b = rd.randint(10, 99)
                    c = a + b
                    answer = int(input(f"{a} + {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} + {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} + {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:
                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 3:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(100, 999)
                    b = rd.randint(100, 999)
                    c = a + b
                    answer = int(input(f"{a} + {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} + {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} + {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:
                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
    elif operation=="substraction":
        if level == 1:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(0, 9)
                    b = rd.randint(0, 9)
                    c = a - b
                    answer = int(input(f"{a} - {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} - {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} - {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:
                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 2:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(10, 99)
                    b = rd.randint(10, 99)
                    c = a - b
                    answer = int(input(f"{a} - {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:

                                        print(f"{a} - {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} - {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:

                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 3:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(100, 999)
                    b = rd.randint(100, 999)
                    c = a - b
                    answer = int(input(f"{a} - {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} - {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} - {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:
                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
    elif operation=="multiplication":
        if level == 1:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(0, 9)
                    b = rd.randint(0, 9)
                    c = a * b
                    answer = int(input(f"{a} x {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} x {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} x {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:
                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 2:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(10, 99)
                    b = rd.randint(10, 99)
                    c = a * b
                    answer = int(input(f"{a} x {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} x {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} x {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break

                                except Exception:

                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 3:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(100, 999)
                    b = rd.randint(100, 999)
                    c = a * b
                    answer = int(input(f"{a} x {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} x {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} x {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:

                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
    elif operation=="division":
        if level == 1:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(1, 9)
                    b = rd.randint(1, 9)
                    c = a / b
                    c = round(c,1)
                    answer = int(input(f"{a} / {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} / {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} / {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:
                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 2:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(10, 99)
                    b = rd.randint(10, 99)
                    c = a / b
                    c = round(c,1)
                    answer = int(input(f"{a} / {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} / {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} / {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:

                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
        elif level == 3:
            q_counter = 0
            a_counter = 0
            f_counter = 0
            while True:
                try:
                    bug_counter = 0
                    if q_counter == 5:
                        print(f"Score: {a_counter}")
                        break
                    a = rd.randint(100, 999)
                    b = rd.randint(100, 999)
                    c = a / b
                    c = round(c,1)
                    answer = int(input(f"{a} / {b} ="))
                    while True:
                        try:
                            if answer == c:
                                q_counter += 1
                                a_counter += 1
                                break
                            if bug_counter == 1:
                                break
                            else:
                                raise Exception()
                        except Exception:
                            print("EEE")
                            f_counter += 1
                            ff_counter = 0
                            bug_counter = 0
                            while True:
                                try:
                                    if ff_counter == 2:
                                        print(f"{a} / {b} = {c}")
                                        q_counter += 1
                                        bug_counter = 1
                                        break
                                    else:
                                        answer = int(input(f"{a} / {b} ="))
                                        if answer != c:
                                            print("EEE")
                                            raise Exception()
                                        else:
                                            break
                                except Exception:

                                    ff_counter += 1
                                    pass
                except (Exception, ValueError):
                    pass
main()