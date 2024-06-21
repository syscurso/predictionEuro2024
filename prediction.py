import random

# Definiendo la fuerza histórica basada en el rendimiento pasado
team_strengths = {
    "Germany": 0.9, "Albania": 0.3, "Austria": 0.5, "Belgium": 0.7, "Croatia": 0.6,
    "Czechia": 0.4, "Denmark": 0.5, "England": 0.8, "France": 0.85, "Georgia": 0.2,
    "Hungary": 0.4, "Italy": 0.8, "Netherlands": 0.8, "Poland": 0.5, "Portugal": 0.85,
    "Romania": 0.4, "Scotland": 0.4, "Serbia": 0.5, "Slovakia": 0.3, "Slovenia": 0.3,
    "Spain": 0.85, "Switzerland": 0.6, "Türkiye": 0.5, "Ukraine": 0.4
}

# Grupos reales de la Eurocopa 2024
groups = {
    "Group A": ["Germany", "Scotland", "Hungary", "Switzerland"],
    "Group B": ["Spain", "Croatia", "Italy", "Albania"],
    "Group C": ["France", "Netherlands", "Romania", "Austria"],
    "Group D": ["Belgium", "Serbia", "Denmark", "Poland"],
    "Group E": ["Portugal", "Türkiye", "Slovakia", "Slovenia"],
    "Group F": ["England", "Czechia", "Ukraine", "Georgia"]
}

# Función para simular un partido basado en la fuerza histórica
def simulate_match(team1, team2):
    prob_team1_wins = team_strengths[team1] / (team_strengths[team1] + team_strengths[team2])
    return team1 if random.random() < prob_team1_wins else team2

def simulate_group_stage(groups):
    group_results = {}
    third_places = []
    for group, teams in groups.items():
        sorted_teams = sorted(teams, key=lambda x: team_strengths[x], reverse=True)
        group_results[group] = sorted_teams[:3]  # Top 3 teams from each group
        third_places.append((group, sorted_teams[2]))  # Adding the third placed team with group info

    third_places_sorted = sorted(third_places, key=lambda x: team_strengths[x[1]], reverse=True)
    best_third_places = third_places_sorted[:4]  # Best 4 third-placed teams
    return group_results, best_third_places

def determine_knockout_matches(group_results, best_third_places):
    third_groups = [x[0] for x in best_third_places]

    # Determinando los emparejamientos de octavos de final según las combinaciones de terceros lugares
    knockout_stage = [
        (group_results["Group A"][0], group_results["Group C"][1]),
        (group_results["Group D"][1], group_results["Group E"][1]),
        (group_results["Group D"][0], group_results["Group F"][1]),
        (group_results["Group A"][1], group_results["Group B"][1]),
        (group_results["Group B"][0], best_third_places[3][1]),
        (group_results["Group F"][0], best_third_places[0][1]),
        (group_results["Group E"][0], best_third_places[1][1]),
        (group_results["Group C"][0], best_third_places[2][1]),

    ]
    
    return knockout_stage

def simulate_round(teams):
    winners = []
    for i in range(0, len(teams), 2):
        winner = simulate_match(teams[i], teams[i+1])
        winners.append(winner)
    return winners

def simulate_tournament(group_results, best_third_places):
    rounds = ["Octavos de Final", "Cuartos de Final", "Semifinales", "Final"]
    
    # Obtener los emparejamientos correctos de octavos de final
    knockout_stage = determine_knockout_matches(group_results, best_third_places)
    
    current_round = [team for pair in knockout_stage for team in pair]  # Flatten the list
    for round_name in rounds:
        print(f"\n{round_name}:")
        if len(current_round) == 1:
            break  # Stop if only one team is left
        for match in range(0, len(current_round), 2):
            print(f"{current_round[match]} vs {current_round[match+1]}")
        current_round = simulate_round(current_round)
        print(f"\nGanadores de {round_name}: {current_round}")
    print(f"\nEl ganador del torneo es: {current_round[0]}")

# Simular la fase de grupos
group_results, best_third_places = simulate_group_stage(groups)

# Mostrar los ganadores de grupos, segundos lugares y los mejores terceros lugares
print("Ganadores de Grupos y Segundos Lugares:")
for group, winners in group_results.items():
    print(f"{group}: 1º {winners[0]}, 2º {winners[1]}")
print(f"Mejores terceros lugares: {[team[1] for team in best_third_places]}")

# Simular el torneo a partir de los ganadores de grupos y mejores terceros lugares
simulate_tournament(group_results, best_third_places)
