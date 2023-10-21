import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.transforms as transforms
import matplotlib.patheffects as pe
import pandas as pd
import seaborn as sns
import numpy as np
import global_config

def plot_bar_consolidado(df: pd.DataFrame, col: str, ylabel: str, title: str = None, legend: bool = False, grid: bool = True, output_mean_line: bool = False, output_median_line: bool = False):
  ordenados = df.sort_values(by=col, ascending=False)
  top15 = ordenados.head(15)

  plt.figure(figsize=(12, 8))

  ax = sns.barplot(data = top15, x = top15.pais, y = col, palette="tab10")
  ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.2f}'))
  ax.set_xlabel('País', fontdict = global_config.fontconfig, labelpad = global_config.padding)
  ax.set_ylabel(ylabel, fontdict = global_config.fontconfig, labelpad = global_config.padding)
  ax.bar_label(ax.containers[0], label_type='edge', fontsize=9, fmt='{:,.2f}', rotation=15, color='#000', path_effects=[pe.withStroke(linewidth=2, foreground="#ccc")])

  if (output_mean_line) :
    media = top15[col].mean()
    plt.axhline(y = np.nanmean(top15[col]), color='red', linestyle='-.', label='Média', linewidth=1.5)
    trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
    ax.text(1.12, media, "{:,.2f}".format(media), color="red", transform=trans, ha="right", va="center", fontsize=9, path_effects=[pe.withStroke(linewidth=1.5, foreground="#ccc")])

  if (output_median_line) :
    media = top15[col].median()
    plt.axhline(y = np.nanmedian(top15[col]), color='blue', linestyle='-.', label='Médiana', linewidth=1.5)
    trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
    ax.text(1.12, media, "{:,.2f}".format(media), color="blue", transform=trans, ha="right", va="center", fontsize=9, path_effects=[pe.withStroke(linewidth=1.5, foreground="#ccc")])

  if (title != None):
      ax.set_title(title, fontdict=global_config.fontconfig,
              pad=global_config.padding)

  if (grid) :
    plt.grid(color='#ccc', linestyle='dashed', linewidth=1)

  if (legend) :
    plt.legend(title = 'Legenda', loc = 'upper left', bbox_to_anchor = (1, 1), title_fontproperties = global_config.fontconfig)

  plt.ylim(0, top15[col].max() + top15[col].max() * 0.05)
  plt.box(False)
  plt.xticks(rotation=60)

  plt.show()