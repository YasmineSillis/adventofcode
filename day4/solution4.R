input <- "bgvyzdsv"


number <- 0
repeat {
  a <- paste(input, number, sep = "")
  res <- digest::digest(a, algo = "md5", serialize = FALSE)
  r <- strsplit(res, "")
  if (r[[1]][1]=="0" && r[[1]][2]=="0" && r[[1]][3]=="0" && r[[1]][4]=="0" && r[[1]][5]=="0" && r[[1]][6]=="0")  {
    break
  }
  number <- number + 1
}

print(number)