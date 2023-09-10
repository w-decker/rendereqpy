import matplotlib.pyplot as plt

def rendereq(latex):
    """
    Render a LaTeX equation as a matplotlib figure.
    """

    PNG = 'output.png'

    # set plt params
    fig=plt.figure()
    plt.axis('off')
    plt.text(0.5, 0.5, f'${latex}$', size=50, ha='center', va='center')

    # make eq
    plt.savefig(PNG, format='png', bbox_inches='tight', pad_inches=0.4, dpi=200)
    plt.close(fig)

    return(PNG)

