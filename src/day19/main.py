import copy
from functools import reduce


def process(workflows: {str: ({(str, str, int): str}, str)}, rating: {str: int}, curr: str) -> bool:
    if curr == "A":
        return True
    if curr == "R":
        return False

    workflow, default = workflows[curr]
    for condition, nxt in workflow.items():
        match condition[1]:
            case ">":
                matches_condition = rating[condition[0]] > condition[2]
            case "<":
                matches_condition = rating[condition[0]] < condition[2]
            case _:
                raise NotImplemented
        if matches_condition:
            return process(workflows, rating, nxt)

    return process(workflows, rating, default)


def partition(
        workflows: {str: ({(str, str, int): str}, str)},
        curr: str,
        variables: {str: (int, int)},
) -> int:
    res = 0

    if curr == "A":
        return reduce(
            lambda a, b: a * b,
            [(x[1] - x[0]) for x in variables.values() if x[1] > x[0]],
        )
    if curr == "R":
        return res

    workflow, default = workflows[curr]
    for condition, nxt in workflow.items():
        match condition[1]:
            case ">":
                vars_if_true = copy.copy(variables)
                vars_if_true[condition[0]] = (condition[2] + 1, vars_if_true[condition[0]][1])
                variables[condition[0]] = (variables[condition[0]][0], condition[2] + 1)
            case "<":
                vars_if_true = copy.copy(variables)
                vars_if_true[condition[0]] = (vars_if_true[condition[0]][0], condition[2])
                variables[condition[0]] = (condition[2], variables[condition[0]][1])
        res += partition(workflows, nxt, vars_if_true)
    return res + partition(workflows, default, variables)


def main():
    unparsed_workflows, ratings = open("data.in").read().split("\n\n")

    workflows = {}
    for w in unparsed_workflows.split("\n"):
        name, rest = w.strip("}").split("{")
        rules = {}
        for rule in rest.split(",")[:-1]:
            rule, name_next = rule.split(":")
            rules[(rule[0], rule[1], int(rule[2:]))] = name_next
        otherwise = rest.split(",")[-1]

        workflows[name] = (rules, otherwise)

    res = 0
    for rating in ratings.split("\n"):
        rating = {k: int(v) for k, v in [i.split("=") for i in rating.strip("{").strip("}").split(",")]}
        if process(workflows, rating, "in"):
            res += sum(rating.values())
    print(res)

    print(partition(workflows, "in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}))


if __name__ == '__main__':
    main()
