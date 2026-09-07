#5 Ajuste
print('EJERCICIO 5')
print()
scores_counter = 1
current_score = 0
total_approved_scores = 0
total_denied_scores = 0
average_approved_scores = 0
average_denied_scores = 0
average_all_scores = 0

total_scores = int(input('Ingrese el total de notas: '))
while scores_counter <= total_scores:
    current_score = int(input(f'Ingrese la nota numero {scores_counter}: '))
    scores_counter += 1
    if current_score < 70:
        total_denied_scores += 1
        average_denied_scores += current_score
    else:
        total_approved_scores += 1
        average_approved_scores += current_score
        average_all_scores = average_all_scores + (current_score / total_scores)
if total_denied_scores == 0:
    print('No hay notas desaprobadas')
else:
    average_denied_scores = average_denied_scores / total_denied_scores
if total_approved_scores == 0:
    print('No hay notas aprobadas')
else:
    average_approved_scores = average_approved_scores / total_approved_scores
print(f'El estudiante tiene esta cantidad de notas aprobadas: {total_approved_scores}')
print(f'Este es el promedio de notas aprobadas: {average_approved_scores}')
print(f'El estudiante tiene esta cantidad de notas desaprobadas: {total_denied_scores}')
print(f'Este es el promedio de notas desaprobada: {average_denied_scores}')
print(f'Este es el promedio total de notas: {average_all_scores}')