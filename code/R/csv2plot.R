list_files <- list.files(
			 path="./data",
			 pattern=".*\.csv"
)

for (file in list_files) {
	file_outhead <- strsplit(file,".")
	pdf(paste(file_outhead , ".pdf",sep=""))
	data <- read.csv(file)
	
	plot(data,xlab="lg2 n",ylab="time in sec",main=paste("plot of" , file_outhead))
	dev.off()
}
