



# =========================================================================================
# Spare Code Snippets TODO - work out what these do exactly
# =========================================================================================

# Buttons
# fig.update_layout(
# 					# updatemenus=[dict(
# 					# 					type = "buttons",
# 					# 					direction = "left",
# 					# 					buttons=list([
# 					# 						dict(
# 					# 							args=["type", "surface"],
# 					# 							label="Hide Weekends",
# 					# 							method="restyle"
# 					# 							),
# 					# 						dict(
# 					# 							args=["type", "heatmap"],
# 					# 							label="Show Weekends",
# 					# 							method="restyle"
# 					# 							)]),
# 					# 					pad={"r": 10, "t": 10},
# 					# 					showactive=True,
# 					# 					x=0.11,
# 					# 					xanchor="left",
# 					# 					y=1.1,
# 					# 					yanchor="top"
# 					# 				),],
# 					)


# def remove_empty_dates(fig, share_df):
# 	# removing all empty dates
# 	dt_all = pd.date_range(start=share_df.index[0],end=share_df.index[-1])				# build complete timeline from start date to end date
# 	dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(share_df.index)]			# retrieve the dates that ARE in the original datset
# 	dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]	# define dates with missing values
# 	fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
# 	fig.update_layout(xaxis_rangebreaks=[dict(values=dt_breaks)])						# Removes anny dates without data - but i need to test this
# 	return fig


# for the relative column size
# relative_total = sum(plotly_schema['chart_heights'])
# for pos, relative_height in enumerate(plotly_schema['chart_heights']):
# 	proportional_height = relative_height / relative_total
# 	plotly_schema['chart_heights'][pos] = proportional_height


