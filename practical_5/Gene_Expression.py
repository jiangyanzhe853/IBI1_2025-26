import matplotlib.pyplot as plt

# Initialize gene expression dictionary
gene_expression = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
print("Initial gene expression:", gene_expression)

# Add MYC gene to the dictionary
gene_expression["MYC"] = 11.6
print("Updated with MYC:", gene_expression)

# Plot bar chart for gene expression
genes, expressions = list(gene_expression.keys()), list(gene_expression.values())
plt.figure(figsize=(8,5))
plt.bar(genes, expressions, color='#4CAF50')
plt.xlabel('Gene'), plt.ylabel('Expression Level'), plt.title('Gene Expression Levels')
plt.xticks(rotation=45), plt.tight_layout(), plt.show()

# Query expression level of target gene (TP53)
gene_of_interest = "TP53"
print(f"Expression of {gene_of_interest}: {gene_expression[gene_of_interest] if gene_of_interest in gene_expression else 'Not found'}")

# Calculate average expression level
avg_expression = sum(expressions) / len(expressions)
print(f"Average expression level: {avg_expression:.2f}")