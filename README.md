This project is a Python-based Indoor Campus Navigation System that helps users find 
the shortest path between two locations inside a building. The system stores rooms, 
corridors, stairs, and floors as a graph and uses the Breadth-First Search (BFS) 
algorithm to calculate the shortest route.

Features:
• Shortest path finding using BFS
• Partial name search (e.g., "lab" → "Lab-1")
• Step-by-step navigation instructions
• Floor information included
• Console-based easy-to-use interface

Sample Output:
----------------------------------------------
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
----------------------------------------------
