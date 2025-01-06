import polars as pl
import numpy as np

def main():
    # generate a sample dataframe with shape 150 x 5, columns are sepal_length, sepal_width, petal_length, petal_width, species
    df = pl.DataFrame({
        "sepal_length": pl.Series(np.random.normal(5.5, 1.0, 150)),
        "sepal_width": pl.Series(np.random.normal(3.5, 0.5, 150)),
        "petal_length": pl.Series(np.random.normal(4.0, 1.5, 150)),
        "petal_width": pl.Series(np.random.normal(1.2, 0.5, 150)),
        "species": pl.Series(np.random.choice(["Setosa", "Versicolor", "Virginica"], 150))
    })


    # Plot with altair
    chart =  (
        df.plot.point(
            x="sepal_width",
            y="sepal_length",
            color="species",
        )
        .properties(width=500, title="Irises")
        .configure_scale(zero=False)
        .configure_axisX(tickMinStep=1)
    )
    chart.encoding.x.title = "Sepal Width"
    chart.encoding.y.title = "Sepal Length"
    print(chart)


if __name__ == "__main__":
    main()