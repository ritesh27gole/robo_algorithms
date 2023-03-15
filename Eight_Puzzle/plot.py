import numpy as np
import matplotlib.pyplot as plt

data_list = [
    [41.97201943397522, 2.5777223110198975, 4.172761917114258],
    [0.2505931854248047, 0.03906536102294922, 0.05382966995239258],
    [1.24169921875, 0.40172386169433594, 0.4516568183898926],
    [6.252938270568848, 1.5357916355133057, 1.5141375064849854],
    [11.237112283706665, 1.8189122676849365, 3.1505656242370605],
    [19.603272438049316, 0.2570981979370117, 1.8629801273345947],
    [0.03333306312561035, 0.011277914047241211, 0.012478351593017578],
    [30.744733572006226, 0.17162346839904785, 4.356178283691406],
    [29.113986492156982, 0.7434906959533691, 1.7350051403045654],
    [47.96467995643616, 1.7499065399169922, 5.80804967880249]
]

data_array = np.array(data_list)
MTH_avg = 0
MDH_avg = 0
EDH_avg = 0
for i in range(0, len(data_list)):
    MTH_avg += data_list[i][0]
    MDH_avg += data_list[i][1]
    EDH_avg += data_list[i][2]

MTH_avg = MTH_avg/10
MDH_avg = MDH_avg/10
EDH_avg = EDH_avg/10

total = MTH_avg + MDH_avg + EDH_avg
MTH_avg = (MTH_avg/total)*100
MDH_avg = (MDH_avg/total)*100
EDH_avg = (EDH_avg/total)*100

print(MTH_avg, MDH_avg, EDH_avg)

values = [MTH_avg, MDH_avg, EDH_avg]
heuristics = ["Misplaced Tile", "Manhattan Distance", "Euler Distance"]
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(heuristics, values, color ='green',
        width = 0.4)
 
plt.xlabel("")
plt.ylabel("Percentage time taken")
plt.title("Time consumption comparison of different heuristics")
plt.show()
