; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.8341731685562686835" = internal constant [3 x i8] c"%d\00"
@".str.8084496673346794580" = internal constant [3 x i8] c"%f\00"
@".str.8515177546619091338" = internal constant [3 x i8] c"%s\00"
@".str.4313221362129951564" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  br label %"while.cond"
while.cond:
  %".3" = load i32, i32* @"i"
  %".4" = icmp slt i32 %".3", 10
  %".5" = zext i1 %".4" to i32
  %".6" = icmp ne i32 %".5", 0
  br i1 %".6", label %"while.body", label %"while.after"
while.body:
  %".8" = load i32, i32* @"i"
  %".9" = bitcast [3 x i8]* @".str.8341731685562686835" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  %".11" = bitcast [2 x i8]* @".str.4313221362129951564" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11")
  %".13" = load i32, i32* @"i"
  %".14" = add i32 %".13", 1
  store i32 %".14", i32* @"i"
  br label %"while.cond"
while.after:
  ret void
}

@"i" = common global i32 0