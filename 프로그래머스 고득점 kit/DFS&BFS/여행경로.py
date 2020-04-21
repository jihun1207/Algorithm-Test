def solution(tickets):
    routes = {}
    for ticket in tickets:
        routes[ticket[0]] = routes.get(ticket[0], []) + [ticket[1]]

    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())

    return path[::-1]