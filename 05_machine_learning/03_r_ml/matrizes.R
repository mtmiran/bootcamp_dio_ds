#           matriz; c (concatenar); numero de linhas; numero de colunas      
MATRIx_A <- matrix(c(2,4,3,1,5,7), nrow = 2, ncol = 3, byrow = TRUE)
print(MATRIx_A)

MATRIx_B <- matrix(c(2,4,3,7,5,12), nrow = 2, ncol = 3, byrow = TRUE)
print(MATRIx_B)

# multiplicação de matrizes
print(MATRIx_A * MATRIx_B)
