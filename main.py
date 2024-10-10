#Variable 
interDistance = 0
def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    # TODO
    global interDistance
    interDistance = ((num_pillars - 1) * gap_pillars * 100) + (num_pillars * pillar_width) - (pillar_width * 2)
    # Refactorizado  interDistance = ((num_pillars - 1) * gap_pillars * 100) + (num_pillars - 2) * pillar_width
    return interDistance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(interDistance)