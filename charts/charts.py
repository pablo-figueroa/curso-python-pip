import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    
    ax.pie(values, labels=labels, autopct='%1.2f%%')
    ax.set_xlabel('Etiqueta X')
    ax.set_ylabel('Etiqueta Y')
    
    plt.title('Pie Chart')
    plt.savefig('pie.png')
    plt.close()