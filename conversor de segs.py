segs_str=input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs=int(segs_str)

semanas=total_segs//604800
segs_rest_semanas=total_segs%604800
dias=segs_rest_semanas//86400
segs_rest_dias=segs_rest_semanas%86400
horas=segs_rest_dias//3600
segs_rest_horas=segs_rest_dias%3600
minutos=segs_rest_horas//60
segs_rest_final=segs_rest_horas%60

print(semanas,"semanas,",dias,"dias,",horas,"horas,",minutos,"minutos e",segs_rest_final,"segundos.")
