list_files <- list.files(
			 path="./data",
			 pattern=".*\.csv"
)

for (file in list_files) {
	file_outhead <- strsplit(file,".")
	svg(file_outhead + ".svg")
	data <- read.csv(file)
	plot(data,xlab="lg2 n",ylab="time in sec",main="plot of " + file_outhead)
	dev.off()
}
