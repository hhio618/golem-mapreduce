# Golem map reduce 
![golem-mr](https://user-images.githubusercontent.com/1272158/121239662-c599fc80-c8ae-11eb-9cfb-5c5f72c448ba.png)

## Todo's
- [X] Add core functionality
- [X] Add mapper using Golem workers
- [ ] Local reducer implementation
- [ ] A mechanism to run local map reduce functions on remote golem nodes

## Intro
The MapReduce algorithm contains two important tasks, namely Map and Reduce.

    The map task is done by means of Mapper Class
    The reduce task is done by means of Reducer Class.

Mapper class takes the input, tokenizes it, maps and sorts it. The output of Mapper class is used as input by Reducer class, which in turn searches matching pairs and reduces them.
Mapper Reducer Class

MapReduce implements various mathematical algorithms to divide a task into small parts and assign them to multiple systems. In technical terms, MapReduce algorithm helps in sending the Map & Reduce tasks to appropriate servers in a cluster.

### License

This project is available under the Apache 2.0 license. 
See the [LICENSE](LICENSE) file for details.

