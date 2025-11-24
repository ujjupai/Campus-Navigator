Description

This project is a Python-based Indoor Navigation System that helps users find the shortest path between two locations inside a multi-floor campus building. The system stores rooms, corridors, stairs, and lifts as a graph and uses the Breadth-First Search (BFS) algorithm to calculate the shortest route. It also provides step-by-step directions, floor information, and supports partial name searching (for example, typing “lab” automatically matches “Lab-1”).

Features

Calculates the shortest path using BFS

Supports partial/fuzzy room name search

Provides floor information for each location

Step-by-step walking instructions

Handles multi-floor navigation

Simple, menu-driven console interface

No external libraries required

How It Works

The campus/building layout is stored as a graph.

The user enters the source and destination rooms.

The input is matched to actual room names (even partial names).

BFS is applied to find the shortest route.

The program displays:

List of places visited

Total number of steps

Floor information

Final navigation directions

Sample Output
Route Finder
From: main gate
To: a-201

Interpreted source: Main Gate
Interpreted destination: A-201

========== ROUTE SUMMARY ==========
Total steps: 4
[0] Main Gate (Ground Floor)
[1] Reception (Ground Floor)
[2] Stairs-GF-1F (Between Ground and First Floor)
[3] Corridor-1F-1 (First Floor)
[4] A-201 (First Floor)

---------- DIRECTIONS ----------
- Walk straight from Main Gate to Reception.
- Walk from Reception to Stairs-GF-1F using the stairs.
- Walk straight from Stairs-GF-1F to Corridor-1F-1.
- Walk straight from Corridor-1F-1 to A-201.

You have reached your destination.

Code Structure

CAMPUS_GRAPH – Building layout stored as a graph

FLOOR_INFO – Floor details for each room

shortest_path() – BFS implementation

find_place_by_name() – Partial name matching

describe_path() – Human-readable navigation steps

main() – Console UI and program flow

Requirements

Python 3.x

No additional modules needed

How to Run

Save the code as indoor_navigation.py

Open terminal/command prompt

Run:

python indoor_navigation.py

Learning Outcomes

Understanding graph representation

BFS shortest path algorithm

Applying data structures to real-world problems

User input handling and clean console output

Multi-floor pathfinding logic

Future Enhancements

GUI interface for campus map

Voice navigation

QR code room scanning

Mobile app version

Real-time map updates

Conclusion

This project demonstrates how graph algorithms like BFS can be used to build a working indoor navigation system. It is simple, interactive, and showcases how Python can be used to solve real-life navigation problems inside multi-floor buildings.
