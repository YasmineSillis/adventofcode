input <- "bgvyzdsv"


number <- 0
repeat {
  a <- paste(input, number, sep = "")
  res <- digest::digest(a, algo = "md5", serialize = FALSE)
  if (substr(res, 1, 6) == "000000") {
    break
  }

  number <- number + 1
}

print(number)