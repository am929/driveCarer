package com.example.carerserver.vo;

public class Result<T>  {
    public int code;
    public String msg;
    //因为不清楚data的数据，所以使用泛型表示
    public T data;

    public static <T> Result success(){//无需参数的
        Result result=new Result("suc",0,null) ;
        return result;
    }
    //携带参数的
    public static <T> Result success(T data){//无需参数的
        Result result=new Result("suc",0,data) ;

        return result;
    }

    private Result(String msg,int code,T data){
        this.data=data;
        this.code=code;
        this.msg=msg;
    }

    public static <T> Result fail(){//无需参数的
        Result result=new Result("fail",-1,null) ;
        return result;
    }
    //携带参数的
    public static <T> Result fail(T data){//无需参数的
        Result result=new Result("fail",-1,data) ;

        return result;
    }
}
