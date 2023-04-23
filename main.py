import tkinter as tk
import customtkinter as ctk

LABEL_FONT = ("Roboto Slab", 12, "bold")
FIELD_FONT = ("Roboto Slab", 12, "normal")
def submit():
    # Handle the form submission here
    pass

root = tk.Tk()
root.title("Settings Page")
root.geometry("500x750")

# background_color = "#8B0000"  # Dark red
# text_color = "#FFE4B5"  # Beige
# dropdown_color = "#FF7F50"  # Coral
back_background_color = "#5c4e3f"
parchment_color = "#99846b"
background_color = "#E8DAB2"  # Soft beige
text_color = "#5C4A3B"  # Muted brown
dropdown_color = "#B8A88D"  # Light brown
hover_color = "#bdad9b"

root.configure(bg=back_background_color)

outer_frame = tk.Frame(root)
outer_frame.configure(bg=back_background_color)
outer_frame.pack(fill="both", expand=True)

outer_frame.grid_rowconfigure(0, weight=1)
outer_frame.grid_columnconfigure(0, weight=1)

frame = ctk.CTkFrame(outer_frame)
frame.configure(bg_color=back_background_color, fg_color=parchment_color)
frame.grid(row=0, column=0)

# Skill level
skill_level_label = ctk.CTkLabel(frame, text_color=text_color, justify="r", text="Skill Level:", font=LABEL_FONT, bg_color=parchment_color)
skill_level_label.grid(row=0, column=0, sticky="e", padx=20, pady=20)

skill_level_options = ["Beginner", "Intermediate", "Experienced", "Expert"]
skill_level_dropdown = ctk.CTkOptionMenu(frame, button_hover_color=hover_color, text_color=text_color, corner_radius=6, font=FIELD_FONT, values=skill_level_options, fg_color=dropdown_color, bg_color=parchment_color, button_color=background_color, dynamic_resizing=False,)
skill_level_dropdown.set("Experienced")
skill_level_dropdown.grid(row=0, column=1, sticky="w", padx=20, pady=20)

# Dietary restrictions
dietary_restrictions_label = ctk.CTkLabel(frame, text_color=text_color, text="Dietary Restrictions:", font=LABEL_FONT, bg_color=parchment_color)
dietary_restrictions_label.grid(row=1, column=0, sticky="e", padx=20, pady=20)

dietary_restrictions_options = ["None", "Vegetarian", "Vegan", "Gluten-free", "Other"]
dietary_restrictions_dropdown = ctk.CTkOptionMenu(frame, button_hover_color=hover_color, text_color=text_color, corner_radius=6, values=dietary_restrictions_options, font=FIELD_FONT, fg_color=dropdown_color, bg_color=parchment_color, dynamic_resizing=False, button_color=background_color)
dietary_restrictions_dropdown.set("None")
dietary_restrictions_dropdown.grid(row=1, column=1, sticky="w", padx=20, pady=20)

# Preferences
preferences_label = ctk.CTkLabel(frame, text_color=text_color, text="Preferences:", font=LABEL_FONT)
preferences_label.grid(row=2, column=0, sticky="e", padx=20, pady=20)

preferences_options = ["Italian", "Mexican", "Chinese", "American"]
preferences_dropdown = ctk.CTkOptionMenu(frame, button_hover_color=hover_color, dynamic_resizing=False, text_color=text_color, corner_radius=6, font=FIELD_FONT, values=preferences_options, fg_color=dropdown_color, bg_color=parchment_color, button_color=background_color)
dietary_restrictions_dropdown.set("Italian")
preferences_dropdown.grid(row=2, column=1, sticky="w", padx=20, pady=20)

# Budget time period
budget_time_period_label = ctk.CTkLabel(frame, text_color=text_color, text="Budget Time Period:", font=LABEL_FONT)
budget_time_period_label.grid(row=3, column=0, sticky="e", padx=20, pady=20)

budget_time_period_options = ["Daily", "Weekly", "Monthly", "Yearly"]
budget_time_period_dropdown = ctk.CTkOptionMenu(frame, button_hover_color=hover_color, text_color=text_color, corner_radius=6, font=FIELD_FONT, values=budget_time_period_options, fg_color=dropdown_color, bg_color=parchment_color, dynamic_resizing=False, button_color=background_color)
dietary_restrictions_dropdown.set("Daily")
budget_time_period_dropdown.grid(row=3, column=1, sticky="w", padx=20, pady=20)

# Budget amount
budget_amount_label = ctk.CTkLabel(frame, text_color=text_color, text="Budget Amount:", font=LABEL_FONT)
budget_amount_label.grid(row=4, column=0, sticky="e", padx=20, pady=20)

budget_amount_entry = ctk.CTkEntry(frame, corner_radius=6, text_color=text_color, font=FIELD_FONT, fg_color=dropdown_color, bg_color=parchment_color)
budget_amount_entry.insert(0, "50")
budget_amount_entry.grid(row=4, column=1, sticky="n", padx=20, pady=20)

# Option count
option_count_label = ctk.CTkLabel(frame, text_color=text_color, text="Option Count:", font=LABEL_FONT)
option_count_label.grid(row=5, column=0, sticky="e", padx=20, pady=20)

option_count_options = ["1", "2", "3"]
option_count_dropdown = ctk.CTkOptionMenu(frame, button_hover_color=hover_color, text_color=text_color, corner_radius=6, font=FIELD_FONT, values=option_count_options, dynamic_resizing=False, fg_color=dropdown_color, bg_color=parchment_color, button_color=background_color)
dietary_restrictions_dropdown.set("1")
option_count_dropdown.grid(row=5, column=1, sticky="n", padx=20, pady=20)

# Meal type
meal_type_label = ctk.CTkLabel(frame, text_color=text_color, text="Meal Type:", font=LABEL_FONT)
meal_type_label.grid(row=6, column=0, sticky="e", padx=20, pady=20)

meal_type_options = ["Breakfast", "Lunch", "Weeknight Dinner", "Weekend Dinner", "Snack"]
meal_type_dropdown = ctk.CTkOptionMenu(frame, button_hover_color=hover_color, text_color=text_color, corner_radius=6, font=FIELD_FONT, values=meal_type_options, dynamic_resizing=False, fg_color=dropdown_color, bg_color=parchment_color, button_color=background_color)
dietary_restrictions_dropdown.set("Weeknight Dinner")
meal_type_dropdown.grid(row=6, column=1, sticky="w", padx=20, pady=20)

# Submit button
submit_button = ctk.CTkButton(frame, hover_color=hover_color, font=FIELD_FONT, text_color=text_color, corner_radius=6, text="Submit", command=submit, fg_color=background_color, bg_color=parchment_color)
submit_button.grid(row=7, columnspan=2, pady=20)

root.mainloop()
