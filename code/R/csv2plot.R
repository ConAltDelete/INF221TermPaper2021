list_files <- list.files(
			 path="./data/csv_files/"
)

for (file in list_files) {
	file_outhead <- strsplit(file,"[.]")[[1]]
	data_file <- read.csv(paste("./data/csv_files/",file,sep=""))
	
	print(file)
	
	# maxi <- max(data_file,na.rm = TRUE)

	pdf(paste("./data/pics/",file_outhead , "_sorted.pdf",sep=""))
	plot(x=data_file$"lg2.n",y=data_file$"sorted",type="l",xlab="lg2.n",ylab="time in sec",main=paste("plot of sorted" , file_outhead), ylim = c(0,1.2*max(data_file$"max_sort")))
	points(x=data_file$"lg2.n",y=data_file$"min_sort", pch=6)
	points(x=data_file$"lg2.n", y=data_file$"max_sort", pch=2)
	polygon(x=c(data_file$"lg2.n",rev(data_file$"lg2.n")),y=c(data_file$"sorted" + qnorm(0.8)*sqrt(data_file$"sorted.variance"),rev(data_file$"sorted" - qnorm(0.8)*sqrt(data_file$"sorted.variance"))), col = "#E60026", density= 10, angle = 45 )
	dev.off()

	pdf(paste("./data/pics/",file_outhead , "_reversed.pdf",sep=""))
	plot(x=data_file$"lg2.n",y=data_file$"reversed",type="l",xlab="lg2.n",ylab="time in sec",main=paste("plot of reversed" , file_outhead), ylim = c(0,1.2*max(data_file$"max_rev")))
	points(x=data_file$"lg2.n",y=data_file$"min_rev", pch=6)
	points(x=data_file$"lg2.n", y=data_file$"max_rev", pch=2)
	polygon(x=c(data_file$"lg2.n",rev(data_file$"lg2.n")),y=c(data_file$"reversed" + qnorm(0.8)*sqrt(data_file$"reversed.variance"),rev(data_file$"reversed" - qnorm(0.8)*sqrt(data_file$"reversed.variance"))), col = "#E60026", density= 10, angle = 45 )
	dev.off()

	pdf(paste("./data/pics/",file_outhead , "_random.pdf",sep=""))
	plot(x=data_file$"lg2.n",y=data_file$"random",type="l",xlab="lg2.n",ylab="time in sec",main=paste("plot of random" , file_outhead), ylim = c(0,1.2*max(data_file$"max_rand")))
	points(x=data_file$"lg2.n",y=data_file$"min_rand", pch=6)
	points(x=data_file$"lg2.n", y=data_file$"max_rand", pch=2)
	polygon(x=c(data_file$"lg2.n",rev(data_file$"lg2.n")),y=c(data_file$"random" + qnorm(0.8)*sqrt(data_file$"random.variance"),rev(data_file$"random" - qnorm(0.8)*sqrt(data_file$"random.variance"))), col = "#E60026", density= 10, angle = 45 )
	dev.off()
}
