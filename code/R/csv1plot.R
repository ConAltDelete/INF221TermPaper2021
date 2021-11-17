list_files <- list.files(
			path="./data/csv_files/"
)

case_plot <- function(data, list_names) {
	
	for (t in list_names) {
		pdf(paste("./data/pics/project_hydro_case_",file_outhead,".pdf",sep=""))
		

		
		legend(
	       		x="topleft",
	       		legend=list_names,
	       		col=c(1,2,3)
		)
		
		dev.off()
	}
}

avg_plot <- function(data,list_names) {
	
	legend(
		x="topleft",
		legend=c("average","maximum","minimum")
	)
}

values_names_case = list("sorted","reversed","random")
values_names_avg = list(c("min_sort","min_rev","min_rand"),c("max_sort","max_rev","max_rand"))

str_list_data <- paste("./data/csv_files/",list_files,sep="")

str_list_data <- str_list_data[file.size(str_list_data) > 0]

list_data <- lapply(str_list_data,function(x){read.csv(x,sep=",",na.string=c("NULL","NA","None","-"))})

for (type in values_names_case) {
	pdf(paste("./data/pics/project_hydro_case_",type,".pdf",sep=""))
	
	for (data in list_data) {
		plot(data, type="l")
	}
	legend("topleft",legend=str_list_data)

	dev.off()
}

for (data_name in list_files){
	file_outhead <- strsplit(data_name,"[.]")[[1]][1]
        data_file <- read.csv(paste("./data/csv_files/",data_name,sep=""),na.strings=c("NULL","NA","None","-"))

        data_file[is.na(data_file)] <- 0

        print(file_outhead)

	avg_plot(data_file,values_names_case)

	dev.off()

}
