list_files <- list.files(
			 path="./data/csv_files/"
)

create_file <- function(data,file_name, fig_name, min_name, max_name, pt, scale=1.2, dens = 10, ang = 45) {
	var_name = paste(fig_name,".variance",sep="")
	
	pdf(paste("./data/pics/",file_name , "_",fig_name,".pdf",sep=""))
	plot(x=data$"lg2.n",y=data[[fig_name]],type="l",xlab="lg2.n",ylab="time in sec",main=paste("plot of",fig_name , file_name), ylim = c(0,scale*max(data[[fig_name]] +qnorm(pt)*sqrt(data[[var_name]]))))
	points(x=data$"lg2.n",y=data[[min_name]], pch=6)
	points(x=data$"lg2.n", y=data[[max_name]], pch=2)
	polygon(x=c(data$"lg2.n",rev(data$"lg2.n")),y=c(data[[fig_name]] + qnorm(pt)*sqrt(data[[var_name]]),rev(data[[fig_name]] - qnorm(pt)*sqrt(data[[var_name]]))), col = "#E60026", density= dens, angle = ang )
	legend(x="topleft", legend=c("Average","minimum","maximum",paste(pt,"confidence interval")),lty="l")
	dev.off()
}

for (file in list_files) {
	file_outhead <- strsplit(file,"[.]")[[1]][1]
	data_file <- read.csv(paste("./data/csv_files/",file,sep=""),na.strings=c("NULL","NA","None","-"))
	
	data_file[is.na(data_file)] <- 0

	print(file_outhead)

	prosent <- 0.95
	
	values_names = list(c("sorted","min_sort","max_sort"), c("reversed","min_rev","max_rev"), c("random","min_rand","max_rand"))

	for (t in values_names) {
		create_file(data=data_file,file_name=file_outhead,fig_name=t[1],min_name=t[2],max_name=t[3],pt=prosent)
	}
}
