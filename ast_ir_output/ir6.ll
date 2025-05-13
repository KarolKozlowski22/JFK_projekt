; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.4593572070920732383" = internal constant [3 x i8] c"%d\00"
@".str.1495783277522668851" = internal constant [3 x i8] c"%f\00"
@".str.966308075288711710" = internal constant [3 x i8] c"%s\00"
@".str.8146335450369478114" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %".2" = bitcast [14 x i8]* @".str.5763952219968936785" to i8*
  %"a" = alloca i8*
  store i8* %".2", i8** %"a"
  %".4" = load i8*, i8** %"a"
  %".5" = bitcast [2 x i8]* @".str.8146335450369478114" to i8*
  %".6" = bitcast [3 x i8]* @".str.966308075288711710" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8* %".4")
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".5")
  ret void
}

@".str.5763952219968936785" = internal constant [14 x i8] c"Hello, World!\00"