n, m = input().split()
n = int(n)
m = int(m)
edges = [set(input().split()) for i in range(m)]

component = {'1'}

for vertex in range(n):
    for edge in edges:
        if edge & component:
            component.update(edge)

component = [int(i) for i in component]
component.sort()
print(len(component))
print(*component)