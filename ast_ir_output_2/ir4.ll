; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.5790171083117608925" = internal constant [3 x i8] c"%d\00"
@".str.3106326101400431079" = internal constant [3 x i8] c"%f\00"
@".str.8444532226840933137" = internal constant [3 x i8] c"%s\00"
@".str.3514099826871306073" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %".2" = call i32 @"test_scope"()
  %".3" = call i32 @"test_local_scope"()
  ret void
}

@"x" = internal global i32 10
define i32 @"test_scope"()
{
entry:
  %".2" = load i32, i32* @"x"
  %".3" = bitcast [3 x i8]* @".str.5790171083117608925" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  %".5" = bitcast [2 x i8]* @".str.3514099826871306073" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5")
  ret i32 0
}

define i32 @"test_local_scope"()
{
entry:
  %"x" = alloca i32
  store i32 20, i32* %"x"
  %".3" = load i32, i32* %"x"
  %".4" = bitcast [3 x i8]* @".str.5790171083117608925" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  %".6" = bitcast [2 x i8]* @".str.3514099826871306073" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  ret i32 0
}
