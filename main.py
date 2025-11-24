from collections import deque

# =====================================
# 1. CAMPUS / BUILDING MAP (GRAPH)
# =====================================

# Each key is a place; the list contains directly connected places.
# Replace this with your real campus/building layout.

CAMPUS_GRAPH = {
    # Ground Floor
    "Main Gate": ["Reception"],
    "Reception": ["Main Gate", "A-101", "A-102", "Stairs-GF-1F", "Sports Room"],
    "A-101": ["Reception", "A-102"],
    "A-102": ["Reception", "A-101", "A-103"],
    "A-103": ["A-102", "Clubs Room"],
    "Clubs Room": ["A-103"],
    "Sports Room": ["Reception"],

    # First Floor
    "Stairs-GF-1F": ["Reception", "Corridor-1F-1", "Lift-1"],
    "Lift-1": ["Corridor-1F-1", "Stairs-GF-1F"],
    "Corridor-1F-1": ["Stairs-GF-1F", "Lift-1", "A-201", "A-202", "Faculty Room-1"],
    "A-201": ["Corridor-1F-1"],
    "A-202": ["Corridor-1F-1", "Lab-1"],
    "Lab-1": ["A-202"],
    "Faculty Room-1": ["Corridor-1F-1"],

    # Second Floor
    "Stairs-1F-2F": ["Corridor-1F-1", "Corridor-2F-1"],
    "Corridor-2F-1": ["Stairs-1F-2F", "A-301", "A-302", "HOD Cabin-1"],
    "A-301": ["Corridor-2F-1"],
    "A-302": ["Corridor-2F-1"],
    "HOD Cabin-1": ["Corridor-2F-1"],
}

# Floor information for each place (for nicer directions)
FLOOR_INFO = {
    "Main Gate": "Ground Floor",
    "Reception": "Ground Floor",
    "A-101": "Ground Floor",
    "A-102": "Ground Floor",
    "A-103": "Ground Floor",
    "Clubs Room": "Ground Floor",
    "Sports Room": "Ground Floor",

    "Stairs-GF-1F": "Between Ground and First Floor",
    "Lift-1": "First Floor",
    "Corridor-1F-1": "First Floor",
    "A-201": "First Floor",
    "A-202": "First Floor",
    "Lab-1": "First Floor",
    "Faculty Room-1": "First Floor",

    "Stairs-1F-2F": "Between First and Second Floor",
    "Corridor-2F-1": "Second Floor",
    "A-301": "Second Floor",
    "A-302": "Second Floor",
    "HOD Cabin-1": "Second Floor",
}


# =====================================
# 2. SHORTEST PATH USING BFS
# =====================================

def shortest_path(graph, start, goal):
    """
    Find the shortest path between start and goal using BFS.
    Returns a list of places representing the path, or None if no path exists.
    """
    if start not in graph or goal not in graph:
        return None

    queue = deque()
    queue.append(start)
    visited = {start: None}  # node -> parent

    while queue:
        current = queue.popleft()

        if current == goal:
            # Reconstruct path from goal to start
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            path.reverse()
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return None


# =====================================
# 3. HELPER FUNCTIONS
# =====================================

def find_place_by_name(partial_name):
    """
    Fuzzy search for a place using a partial, case-insensitive name.
    Example: "hod" -> "HOD Cabin-1" if it exists.
    """
    partial_name = partial_name.lower().strip()
    candidates = []

    for place in CAMPUS_GRAPH.keys():
        if partial_name in place.lower():
            candidates.append(place)

    if not candidates:
        return None

    # For now, return the first match.
    return candidates[0]


def describe_path(path):
    """
    Print a human-readable description of the path and step-by-step directions.
    """
    if not path:
        print("No path found between the selected locations.")
        return

    print("\n========== ROUTE SUMMARY ==========")
    print(f"Total steps: {len(path) - 1}")
    print("Path:")
    for i, place in enumerate(path):
        floor = FLOOR_INFO.get(place, "Unknown Floor")
        print(f"  [{i}] {place}  ({floor})")

    print("\n---------- DIRECTIONS ----------\n")

    for i in range(len(path) - 1):
        current = path[i]
        nxt = path[i + 1]

        current_floor = FLOOR_INFO.get(current, "Unknown Floor")
        next_floor = FLOOR_INFO.get(nxt, "Unknown Floor")

        if "Stairs" in current or "Stairs" in nxt:
            print(f"- Walk from {current} to {nxt} using the stairs.")
        elif "Lift" in current or "Lift" in nxt:
            print(f"- Walk from {current} to {nxt} and use the lift.")
        elif current_floor != next_floor:
            print(f"- Walk from {current} ({current_floor}) to {nxt} ({next_floor}).")
        else:
            print(f"- Walk straight from {current} to {nxt}.")

    print("\nYou have reached your destination ✅\n")


# =====================================
# 4. MAIN CONSOLE APPLICATION
# =====================================

def main():
    print("============================================")
    print("   Indoor Navigation System (Campus Demo)   ")
    print("============================================")

    while True:
        print("\nMenu:")
        print("1. Show all known locations")
        print("2. Find route between two locations")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print("\nKnown locations:")
            for place in CAMPUS_GRAPH.keys():
                floor = FLOOR_INFO.get(place, "Unknown Floor")
                print(f"- {place} ({floor})")

        elif choice == "2":
            print("\nRoute Finder")
            src_input = input("From (e.g., Main Gate, A-101, hod, lab): ").strip()
            dst_input = input("To   (e.g., A-201, Clubs Room, sports): ").strip()

            src = find_place_by_name(src_input)
            dst = find_place_by_name(dst_input)

            if src is None:
                print(f"Source location not found for: '{src_input}'.")
                continue
            if dst is None:
                print(f"Destination location not found for: '{dst_input}'.")
                continue

            print(f"\nInterpreted source:      {src}")
            print(f"Interpreted destination: {dst}")

            path = shortest_path(CAMPUS_GRAPH, src, dst)
            describe_path(path)

        elif choice == "3":
            print("Exiting Indoor Navigation System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
