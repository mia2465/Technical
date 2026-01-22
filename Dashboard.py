import panel as pn
import pandas as pd
import matplotlib.pyplot as plt


pn.extension()


data_total = pn.pane.DataFrame(pd.read_csv('cell_data_total.csv'))

initial_analysis = pn.pane.DataFrame(pd.read_csv('initial_analysis.csv'))


population_row = pn.Row(pn.pane.Markdown( """Logistic euqation for predicting  \
                                          response based on cell percentages 
                                         in sample(assuming null is no response): 
                                         b0 =-0.4982510890322582, 
                                         [b, cd8_t, cd4_t, nk ,monocyte] =  [-1.83214622 -0.44636613  2.01727346  0.12665097 -0.36366317]"""),
                        pn.pane.Image('boxplot_comparison.png',
                        sizing_mode="stretch_width",width=1200,
                                        height=700),
                        pn.pane.DataFrame(pd.read_csv('p_values.csv')),
                        pn.pane.Markdown("""cell types b_cell,cd8_t_cell, and cd4_t_cell
                                          show significant differences in realtive frequencies, 
                                         each with a p < .05. nk and monocyte cells do not"""))

sub_query_row = pn.Row(pd.read_csv('sub_query.csv'),
                       pd.read_csv('sub_query_project.csv'),
                       pd.read_csv('sub_query_responders.csv'),
                       pd.read_csv('sub_query_gender.csv'))

tabs = pn.Tabs(("Total Data Set", data_total),
              ("Initial Analysis", initial_analysis),
              ("Population Analysis", population_row),
              ("Subset Analysis", sub_query_row))

tabs.servable()
