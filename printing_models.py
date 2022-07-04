import printing_functions
    
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#define the function print_models() with two paramenters
#call print_models() and pass it the two lists
# then we call show_completed_models() and pass it to the list of completed models so it can report the printed models 

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
