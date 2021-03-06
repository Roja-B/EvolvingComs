# Important Note: Arrays in R are labeled from 1 to n, but vertices in igraph are labled from 0 to n-1. This means V(G)[0]$name = V(G)$name[1]


#PATH = "/media/data2/roja/Balatarin/CompleteRun3/Results/"
source("PARAMETERS")
library(igraph)
# read graph from file
G<-read.graph("unipartite.txt", format="ncol")
# cluster the base graph and save membership information
source("clustergraph.R")
results <- clustergraph(G)
memberships <- list(membership=results$membership,csize=results$csize)
modularity <- results[3]
# save the names of vertices belonging to each cluster in a separate file.
N= length(memberships$csize)
source("vertexwrite.R")
vertexwrite(memberships,G,'memberships')
write(c(getwd(),N,modularity[[1]]),file=paste(PATH,"/Results/NumComsAndModularities",sep=""),ncolumns=3,append=TRUE)

