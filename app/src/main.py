import re


def main(model, prompt):
    response = model.generate_content(prompt)

    ret =[]
    while True:
        try:
            _, end = (re.search(r"\n", response.text)).regs[0]
        except AttributeError:
            ret.append(response[:])
            break
        ret.append(response[:end])
        response = response[end:]
    return ret


if __name__ == "__main__":
    main("dummy1", "dummy2")