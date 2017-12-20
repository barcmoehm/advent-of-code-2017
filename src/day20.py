class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def __str__(self):
        return "pos: " + str(self.p) + "; v: " + str(self.v) + "; a: " + str(self.a)

    def __repr__(self):
        return self.__str__()

    def update(self):
        v1 = self.v[0] + self.a[0]
        v2 = self.v[1] + self.a[1]
        v3 = self.v[2] + self.a[2]
        self.v = (v1, v2, v3)

        pos1 = self.p[0] + self.v[0]
        pos2 = self.p[1] + self.v[1]
        pos3 = self.p[2] + self.v[2]
        self.p = (pos1, pos2, pos3)

    def dist(self):
        return sum([abs(n) for n in self.p])


particles = {}
file = open("day20.txt")
i = 0
for line in file:
    inp = line.strip().split(", ")
    pos = [int(x) for x in inp[0].split("=")[1][1:-1].split(",")]
    vel = [int(x) for x in inp[1].split("=")[1][1:-1].split(",")]
    acc = [int(x) for x in inp[2].split("=")[1][1:-1].split(",")]
    particles[i] = Particle(pos, vel, acc)
    i += 1

while True:
    dist = None
    part = None
    for i, particle in particles.items():
        particle.update()
        if part is None or particle.dist() < dist:
            part = i
            dist = particle.dist()
    print(part)
