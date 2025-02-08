# Initialize an empty dictionary to store gene information
gene_dict = {}

# Loop to collect user input
while True:
    gene_name = input("Enter a gene name (or type 'exit' to stop): ")
    
    # Condition to break the loop
    if gene_name.lower() == 'exit':
        break
    
    # Get additional information for the gene
    gene_info = input(f"Enter the description for {gene_name}: ")
    
    # Store the information in the dictionary
    gene_dict[gene_name] = gene_info

# Print the final dictionary and description
print("\nFinal Gene Dictionary:")
print(gene_dict)
print("\nThis dictionary stores gene names as keys and their descriptions as values.")
