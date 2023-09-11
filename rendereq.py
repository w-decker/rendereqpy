import matplotlib.pyplot as plt

def rendereq(latex, filename, format='png'):
    """
    Render a LaTeX equation as a matplotlib figure.

    Parameters
    ----------
    latex: str
        String formatted in LaTeX. Note: you MUST use double 
        back-slash (\\) in place of single back-slash

    filename: str
        Name of the output file

    format: str, ('png' | 'pdf') default='png'
        Type of file format 

    """

    OUT = f'{filename}.png'
    if format.lower() == 'pdf':
        format='pdf'
        OUT = f'{filename}.pdf'

    # set plt params
    fig=plt.figure()
    plt.axis('off')
    plt.text(0.5, 0.5, f'${latex}$', size=50, ha='center', va='center')

    # make eq
    plt.savefig(OUT, format=format, bbox_inches='tight', pad_inches=0.4, dpi=200)
    plt.close(fig)

    return(OUT)